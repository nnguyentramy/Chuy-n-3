import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("nhansu.csv")

# 2. Hiển thị dữ liệu ban đầu
print("=== Dữ liệu ban đầu ===")
print(df.head())

# 3. Chuẩn hóa cột HoTen (xóa khoảng trắng thừa)
df['HoTen'] = df['HoTen'].str.strip()

# 4. Chuẩn hóa GioiTinh
df['GioiTinh'] = df['GioiTinh'].str.strip().str.lower()

df['GioiTinh'] = df['GioiTinh'].replace({
    'nam': 'Nam',
    'nữ': 'Nữ',
    'nu': 'Nữ',
    'female': 'Nữ',
    'male': 'Nam'
})
# 5. Chuẩn hóa PhongBan (viết hoa chữ cái đầu)
df['PhongBan'] = df['PhongBan'].str.strip().str.title()

# 6. Đổi tên cột
df = df.rename(columns={
    'MaNV': 'ma_nv',
    'HoTen': 'ho_ten',
    'GioiTinh': 'gioi_tinh',
    'PhongBan': 'phong_ban',
    'Luong': 'luong'
})
# 7. Kết quả sau xử lý
print("\n=== Dữ liệu sau khi chuẩn hóa ===")
print(df.head())

# 8. Lưu file
df.to_csv("nhansu_clean.csv", index=False)

print("\n✔ Đã lưu file nhansu_clean.csv")