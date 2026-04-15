import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# =========================
# Xử lý giá trị thiếu
# =========================

# 1. Giới tính
df["gender"] = df["gender"].fillna("Không rõ")

# 2. Tỷ lệ chuyên cần (dùng median)
median_attendance = df["attendance_rate"].median()
df["attendance_rate"] = df["attendance_rate"].fillna(median_attendance)

# 3. Số điện thoại
df["phone"] = df["phone"].fillna("Chưa cập nhật")

# =========================
# Kiểm tra kết quả
# =========================
print("=== Số lượng giá trị thiếu sau khi xử lý ===")
print(df.isna().sum())

print("\n=== 5 dòng dữ liệu ===")
print(df.head())