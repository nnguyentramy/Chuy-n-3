# Import thư viện pandas để xử lý dữ liệu
import pandas as pd

# Đọc file CSV vào DataFrame
# Lưu ý: file "diem_sinhvien.csv" phải nằm cùng thư mục với file .py hoặc .ipynb
df = pd.read_csv("diem_sinhvien.csv")

# Hiển thị 5 dòng đầu tiên của dữ liệu
print("5 dòng đầu:")
print(df.head())

# Hiển thị 5 dòng cuối cùng của dữ liệu
print("\n5 dòng cuối:")
print(df.tail())

# Hiển thị thông tin tổng quan về dữ liệu
# (số dòng, kiểu dữ liệu, có bị thiếu dữ liệu không)
print("\nThông tin dữ liệu:")
print(df.info())

# Hiển thị thống kê mô tả (chỉ áp dụng cho cột số)
# gồm: count, mean, std, min, max...
print("\nThống kê mô tả:")
print(df.describe())

# Lấy kích thước DataFrame (số dòng, số cột)
print("\nKích thước dữ liệu:", df.shape)

# Lấy danh sách tên các cột
print("Tên các cột:", df.columns.tolist())