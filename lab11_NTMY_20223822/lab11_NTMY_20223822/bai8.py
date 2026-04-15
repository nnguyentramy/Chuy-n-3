# ================================
# 1. IMPORT THƯ VIỆN
# ================================
# pandas: xử lý dữ liệu
# matplotlib: vẽ biểu đồ
# sklearn: mô hình hóa

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# ================================
# 2. ĐỌC DỮ LIỆU
# ================================
# Đọc file CSV vào DataFrame

df = pd.read_csv("student_performance_dirty.csv")

# Hiển thị 5 dòng đầu để kiểm tra
print("=== 5 dòng đầu ===")
print(df.head())


# ================================
# 3. KHÁM PHÁ DỮ LIỆU
# ================================
# Xem thông tin tổng quan

print("\n=== Thông tin dữ liệu ===")
print(df.info())

# Thống kê mô tả các cột số
print("\n=== Thống kê mô tả ===")
print(df.describe())

# Kiểm tra dữ liệu thiếu
print("\n=== Missing values ===")
print(df.isnull().sum())


# ================================
# 4. LÀM SẠCH DỮ LIỆU
# ================================

# 4.1 Xóa dữ liệu trùng
df = df.drop_duplicates()

# 4.2 Lọc điểm hợp lệ (0 → 10)
df = df[(df["score_python"] >= 0) & (df["score_python"] <= 10)]

# 4.3 Bỏ các dòng thiếu dữ liệu quan trọng
df = df.dropna(subset=["attendance_rate", "score_python"])

# 4.4 Chuẩn hóa tên lớp (tránh CNTT1, CNTT-3,...)
df['class_name'] = df['class_name'].str.replace("-", " ")
df['class_name'] = df['class_name'].str.replace("CNTT1", "CNTT 1")

print("\n=== Dữ liệu sau khi làm sạch ===")
print(df.head())


# ================================
# 5. TRỰC QUAN HÓA DỮ LIỆU
# ================================

# ---------- 5.1 Biểu đồ cột ----------
# Nhóm theo lớp và tính điểm trung bình

group_data = df.groupby("class_name")["score_python"].mean()

group_data.plot(kind="bar")
plt.title("Điểm Python trung bình theo lớp")
plt.xlabel("Lớp")
plt.ylabel("Điểm trung bình")
plt.show()


# ---------- 5.2 Histogram ----------
# Xem phân phối điểm

df["score_python"].plot(kind="hist", bins=5)
plt.title("Phân phối điểm Python")
plt.xlabel("Điểm")
plt.ylabel("Tần suất")
plt.show()


# ---------- 5.3 Scatter Plot ----------
# Quan hệ giữa chuyên cần và điểm

df.plot(kind="scatter", x="attendance_rate", y="score_python")
plt.title("Quan hệ giữa chuyên cần và điểm Python")
plt.xlabel("Tỷ lệ chuyên cần (%)")
plt.ylabel("Điểm")
plt.show()


# ================================
# 6. MÔ HÌNH HÓA (LINEAR REGRESSION)
# ================================

# 6.1 Chọn biến
X = df[["attendance_rate"]]   # biến đầu vào
y = df["score_python"]        # biến đầu ra

# 6.2 Chia train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 6.3 Tạo và huấn luyện mô hình
model = LinearRegression()
model.fit(X_train, y_train)

# 6.4 Dự đoán
y_pred = model.predict(X_test)

# 6.5 Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)

print("\n=== Kết quả mô hình ===")
print("MSE:", mse)
print("Hệ số (coef):", model.coef_)
print("Intercept:", model.intercept_)


# ================================
# 7. SO SÁNH KẾT QUẢ
# ================================
print("\n=== So sánh thực tế và dự đoán ===")
for real, pred in zip(y_test, y_pred):
    print(f"Thực tế: {real:.2f} | Dự đoán: {pred:.2f}")