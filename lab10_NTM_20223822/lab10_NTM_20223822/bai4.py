import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# =========================
# Kiểm tra trùng lặp
# =========================

print("=== Số dòng trùng hoàn toàn ===")
print(df.duplicated().sum())

print("\n=== Số dòng trùng theo student_id ===")
print(df.duplicated(subset=["student_id"]).sum())

# =========================
# Xóa trùng lặp
# =========================

# 1. Xóa dòng trùng hoàn toàn
df = df.drop_duplicates()

# 2. Xóa trùng theo student_id (giữ dòng đầu)
df = df.drop_duplicates(subset=["student_id"], keep="first")

# =========================
# Kiểm tra lại
# =========================
print("\n=== Sau khi xử lý ===")
print("Số dòng trùng còn lại:", df.duplicated().sum())
print("Số student_id trùng còn lại:", df.duplicated(subset=["student_id"]).sum())

print("\n=== 5 dòng dữ liệu ===")
print(df.head())