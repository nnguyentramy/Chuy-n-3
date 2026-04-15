import pandas as pd

# Đọc file
df = pd.read_csv("student_performance_dirty.csv")

# 5 dòng đầu
print("=== 5 dòng đầu ===")
print(df.head())

# Thông tin dữ liệu
print("\n=== Thông tin dữ liệu ===")
print(df.info())

# Thống kê mô tả
print("\n=== Thống kê mô tả ===")
print(df.describe())

# Kiểm tra thiếu dữ liệu
print("\n=== Missing values ===")
print(df.isnull().sum())