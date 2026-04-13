import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("khaosat.csv")

# 2. Hiển thị dữ liệu ban đầu
print("=== Dữ liệu ban đầu ===")
print(df.head())

# 3. Chuẩn hóa CoLamThem (dùng map thay replace)
df['CoLamThem'] = df['CoLamThem'].astype(str).str.strip().str.lower()

df['CoLamThem'] = df['CoLamThem'].map({
    'yes': 1, 'y': 1, 'có': 1, 'co': 1,
    'no': 0, 'n': 0, 'không': 0, 'khong': 0
}).astype('Int64')  # kiểu số an toàn (không warning)

# 4. Chuẩn hóa MucDoHaiLong
df['MucDoHaiLong'] = df['MucDoHaiLong'].astype(str).str.strip().str.lower()

df['MucDoHaiLong'] = df['MucDoHaiLong'].replace({
    'rat khong hai long': 1,
    'khong hai long': 2,
    'binh thuong': 3,
    'hai long': 4,
    'rat hai long': 5
})

df['MucDoHaiLong'] = pd.to_numeric(df['MucDoHaiLong'], errors='coerce')

# 5. Đổi tên cột
df = df.rename(columns={
    'MaSV': 'ma_sv',
    'GioHocMoiNgay': 'gio_hoc_moi_ngay',
    'MucDoHaiLong': 'muc_do_hai_long',
    'CoLamThem': 'co_lam_them'
})

# 6. Loại bản ghi không hợp lệ
df = df[df['gio_hoc_moi_ngay'] >= 0]

# 7. Thống kê
print("\n=== Thống kê làm thêm ===")
print(df['co_lam_them'].value_counts())

# 8. Kết quả
print("\n=== Dữ liệu sau khi làm sạch ===")
print(df)

# 9. Lưu file
df.to_csv("khaosat_clean.csv", index=False)

print("\n✔ Đã lưu file khaosat_clean.csv")