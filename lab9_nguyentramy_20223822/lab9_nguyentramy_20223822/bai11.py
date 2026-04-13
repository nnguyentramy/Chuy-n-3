import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("tuyensinh.csv")

print("=== Dữ liệu ban đầu ===")
print(df.head())

# ==============================
# 2. CHUẨN HÓA DỮ LIỆU
# ==============================

# Chuẩn hóa họ tên (viết hoa chữ cái đầu)
df['HoTen'] = df['HoTen'].astype(str).str.strip().str.title()

# Chuẩn hóa giới tính
df['GioiTinh'] = df['GioiTinh'].astype(str).str.strip().str.lower()
df['GioiTinh'] = df['GioiTinh'].replace({
    'nam': 'Nam',
    'male': 'Nam',
    'nữ': 'Nu',
    'nu': 'Nu',
    'female': 'Nu'
}).infer_objects(copy=False)

# Chuẩn hóa ngày sinh
df['NgaySinh'] = pd.to_datetime(df['NgaySinh'], errors='coerce')

# ==============================
# 3. XỬ LÝ GIÁ TRỊ THIẾU
# ==============================

# Điền ngày sinh thiếu bằng trung vị
df['NgaySinh'] = df['NgaySinh'].fillna(df['NgaySinh'].median())

# Điểm → ép kiểu số
for col in ['DiemToan', 'DiemVan', 'DiemAnh']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Điền điểm thiếu bằng trung bình
for col in ['DiemToan', 'DiemVan', 'DiemAnh']:
    df[col] = df[col].fillna(df[col].mean())

# ==============================
# 4. PHÁT HIỆN ĐIỂM BẤT THƯỜNG
# ==============================

for col in ['DiemToan', 'DiemVan', 'DiemAnh']:
    df[col] = df[col].clip(0, 10)

# ==============================
# 5. TÍNH TỔNG ĐIỂM
# ==============================

df['TongDiem'] = df['DiemToan'] + df['DiemVan'] + df['DiemAnh']

# ==============================
# 6. PHÂN NHÓM BẰNG QCUT
# ==============================

df['XepLoai'] = pd.qcut(
    df['TongDiem'],
    q=4,
    labels=['Thap', 'TrungBinh', 'Kha', 'Cao']
)

# ==============================
# 7. THỐNG KÊ THEO KHU VỰC
# ==============================

thongke = df.groupby('KhuVuc').agg(
    SoThiSinh=('MaHS', 'count'),
    DiemTB=('TongDiem', 'mean')
).reset_index()

# ==============================
# 8. HIỂN THỊ KẾT QUẢ
# ==============================

print("\n=== Dữ liệu sau khi làm sạch ===")
print(df.head())

print("\n=== Thống kê theo khu vực ===")
print(thongke)

# ==============================
# 9. LƯU FILE
# ==============================

df.to_csv("tuyensinh_clean.csv", index=False)
thongke.to_csv("tuyensinh_thongke.csv", index=False)

print("\n✔ Đã lưu file tuyensinh_clean.csv")
print("✔ Đã lưu file tuyensinh_thongke.csv")