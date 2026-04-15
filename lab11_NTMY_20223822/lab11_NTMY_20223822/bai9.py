import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# ================================
# 1. Đọc và làm sạch dữ liệu
# ================================
df = pd.read_csv("student_performance_dirty.csv")

df = df.drop_duplicates()
df = df[(df["score_python"] >= 0) & (df["score_python"] <= 10)]
df = df.dropna(subset=["attendance_rate", "score_python"])

# Tạo thêm biến mới
df["high_attendance"] = df["attendance_rate"].apply(lambda x: 1 if x >= 85 else 0)

# ================================
# 2. MODEL 1: dùng 1 biến
# ================================
X1 = df[["attendance_rate"]]
y = df["score_python"]

X1_train, X1_test, y_train, y_test = train_test_split(
    X1, y, test_size=0.3, random_state=42
)

model1 = LinearRegression()
model1.fit(X1_train, y_train)

y_pred1 = model1.predict(X1_test)
mse1 = mean_squared_error(y_test, y_pred1)

# ================================
# 3. MODEL 2: dùng nhiều biến
# ================================
X2 = df[["attendance_rate", "high_attendance"]]

X2_train, X2_test, y_train, y_test = train_test_split(
    X2, y, test_size=0.3, random_state=42
)

model2 = LinearRegression()
model2.fit(X2_train, y_train)

y_pred2 = model2.predict(X2_test)
mse2 = mean_squared_error(y_test, y_pred2)

# ================================
# 4. SO SÁNH
# ================================
print("=== So sánh mô hình ===")
print("Model 1 (1 biến) - MSE:", mse1)
print("Model 2 (nhiều biến) - MSE:", mse2)

if mse2 < mse1:
    print("→ Model 2 tốt hơn")
else:
    print("→ Model 1 tốt hơn")