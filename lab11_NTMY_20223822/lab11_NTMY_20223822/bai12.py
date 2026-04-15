import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

print("=== START ===")

# ================================
# 1. Đọc dữ liệu
# ================================
df = pd.read_csv("student_performance_dirty.csv")

print("Số dòng ban đầu:", len(df))

# ================================
# 2. Làm sạch dữ liệu
# ================================
df = df.drop_duplicates()

# Giữ score hợp lệ
df = df[(df["score_python"] >= 0) & (df["score_python"] <= 10)]

# Xóa thiếu
df = df.dropna(subset=["attendance_rate", "score_python"])

print("Sau khi làm sạch:", len(df))

# ❗ Nếu không đủ dữ liệu thì dừng
if len(df) < 3:
    print("❌ Dữ liệu quá ít để train model")
    exit()

# ================================
# 3. Feature & Target
# ================================
X = df[["attendance_rate"]]   # biến đầu vào
y = df["score_python"]        # biến cần dự đoán

# ================================
# 4. Train/Test
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Train:", len(X_train), "| Test:", len(X_test))

# ================================
# 5. Linear Regression
# ================================
model1 = LinearRegression()
model1.fit(X_train, y_train)

pred1 = model1.predict(X_test)

# ================================
# 6. Decision Tree
# ================================
model2 = DecisionTreeRegressor(max_depth=3, random_state=42)
model2.fit(X_train, y_train)

pred2 = model2.predict(X_test)

# ================================
# 7. Đánh giá
# ================================
mse1 = mean_squared_error(y_test, pred1)
r21 = r2_score(y_test, pred1)

mse2 = mean_squared_error(y_test, pred2)
r22 = r2_score(y_test, pred2)

print("\n=== Linear Regression ===")
print("MSE:", mse1)
print("R2:", r21)

print("\n=== Decision Tree ===")
print("MSE:", mse2)
print("R2:", r22)

# ================================
# 8. So sánh
# ================================
print("\n=== SO SÁNH ===")

if mse1 < mse2:
    print("✔ Linear Regression có MSE tốt hơn")
else:
    print("✔ Decision Tree có MSE tốt hơn")

if r21 > r22:
    print("✔ Linear Regression có R2 tốt hơn")
else:
    print("✔ Decision Tree có R2 tốt hơn")

print("\n=== END ===")