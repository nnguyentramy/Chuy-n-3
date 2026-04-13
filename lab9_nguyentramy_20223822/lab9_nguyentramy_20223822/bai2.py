import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("donhang.csv")

# 2. Hiển thị thông tin
print("=== Thông tin dữ liệu ===")
print(df.info())

print("\n=== 5 dòng đầu ===")
print(df.head())

# 3. Kiểm tra dòng trùng toàn bộ
print("\n=== Số dòng trùng toàn bộ ===")
print(df.duplicated().sum())

# 4. Kiểm tra trùng theo MaDon
print("\n=== Số dòng trùng theo MaDon ===")
print(df.duplicated(subset=['MaDon']).sum())

# 5. Xóa dữ liệu trùng (giữ bản ghi đầu tiên)
df = df.drop_duplicates()
df = df.drop_duplicates(subset=['MaDon'], keep='first')

# 6. Tạo cột ThanhTien
df['ThanhTien'] = df['SoLuong'] * df['DonGia']

# 7. Chuyển NgayDat về datetime để sort chuẩn
df['NgayDat'] = pd.to_datetime(df['NgayDat'])

# 8. Sắp xếp theo ngày tăng dần
df = df.sort_values(by='NgayDat')

# 9. Hiển thị kết quả
print("\n=== Dữ liệu sau khi xử lý ===")
print(df)

# 10. Lưu file
df.to_csv("donhang_clean.csv", index=False)

print("\n✔ Đã lưu file donhang_clean.csv")