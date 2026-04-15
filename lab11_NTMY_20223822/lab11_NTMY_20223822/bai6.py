import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# Làm sạch dữ liệu
df = df.drop_duplicates()

# Lọc điểm hợp lệ
df = df[(df["score_python"] >= 0) & (df["score_python"] <= 10)]

# Bỏ giá trị thiếu
df = df.dropna(subset=["attendance_rate", "score_python"])

# Chọn biến
X = df[["attendance_rate"]]
y = df["score_python"]

# Chia train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Tạo mô hình
model = LinearRegression()

# Huấn luyện
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Đánh giá
mse = mean_squared_error(y_test, y_pred)

print("MSE:", mse)
print("Hệ số (coef):", model.coef_)
print("Intercept:", model.intercept_)