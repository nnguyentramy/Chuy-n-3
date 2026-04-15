import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv("student_performance_dirty.csv")

# Hiển thị 5 dòng đầu
print("=== 5 dòng đầu của dữ liệu ===")
print(df.head())

# Thông tin tổng quan về dữ liệu
print("\n=== Thông tin dữ liệu ===")
df.info()

# Đếm số lượng giá trị thiếu
print("\n=== Số lượng giá trị thiếu ===")
print(df.isna().sum())