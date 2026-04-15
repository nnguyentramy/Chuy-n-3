import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ================================
# 1. Đọc và làm sạch dữ liệu
# ================================
df = pd.read_csv("student_performance_dirty.csv")

df = df.drop_duplicates()
df = df[(df["score_python"] >= 0) & (df["score_python"] <= 10)]
df = df.dropna(subset=["attendance_rate", "score_python"])

# ================================
# 2. Xây dựng mô hình
# ================================
X = df[["attendance_rate"]]
y = df["score_python"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# ================================
# 3. VẼ BIỂU ĐỒ SO SÁNH
# ================================
plt.figure()

# Giá trị thực tế
plt.plot(y_test.values, marker='o', label='Thực tế')

# Giá trị dự đoán
plt.plot(y_pred, marker='x', label='Dự đoán')

plt.title("So sánh giá trị thực tế và dự đoán")
plt.xlabel("Mẫu dữ liệu")
plt.ylabel("Điểm Python")
plt.legend()
plt.show()