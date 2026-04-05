# Import thư viện pandas để làm việc với dữ liệu
import pandas as pd

# Tạo Series chứa điểm của 5 sinh viên
# index là mã sinh viên tương ứng với từng điểm
diem = pd.Series(
    [7.5, 8.0, 6.5, 9.0, 8.5],   # dữ liệu điểm
    index=["SV01", "SV02", "SV03", "SV04", "SV05"]  # chỉ mục (mã SV)
)

# In ra toàn bộ danh sách điểm
print("Danh sách điểm:")
print(diem)

# Lấy 2 phần tử đầu tiên trong Series
print("\nHai phần tử đầu:")
print(diem.head(2))

# Tìm điểm lớn nhất trong Series
print("\nĐiểm lớn nhất:", diem.max())

# Tính điểm trung bình
print("Điểm trung bình:", diem.mean())

# Lọc ra các sinh viên có điểm >= 8
print("\nSinh viên có điểm >= 8:")
print(diem[diem >= 8])