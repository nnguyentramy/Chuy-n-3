import pandas as pd
import glob

# ==============================
# 1. ĐỌC & GHÉP FILE
# ==============================

files = glob.glob("banhang_thang*.csv")

df_list = []

for file in files:
    temp = pd.read_csv(file)

    # ==============================
    # 2. CHUẨN HÓA TÊN CỘT
    # ==============================
    temp.columns = temp.columns.str.strip().str.lower()

    # Map về tên chuẩn
    temp = temp.rename(columns={
        'madon': 'ma_don',
        'mahd': 'ma_don',
        'tensp': 'ten_sp',
        'sanpham': 'ten_sp',
        'ngay': 'ngay_dat',
        'ngaydat': 'ngay_dat',
        'giatien': 'gia',
        'tongtien': 'gia'
    })

    df_list.append(temp)

# Ghép dữ liệu
df = pd.concat(df_list, ignore_index=True)

print("=== Sau khi ghép ===")
print(df.head())

# ==============================
# 3. XỬ LÝ TRÙNG ĐƠN HÀNG
# ==============================

df = df.drop_duplicates(subset='ma_don', keep='first')

# ==============================
# 4. CHUẨN HÓA NGÀY & GIÁ
# ==============================

# Ngày
df['ngay_dat'] = pd.to_datetime(df['ngay_dat'], errors='coerce')

# Giá: bỏ ký tự tiền
df['gia'] = (
    df['gia']
    .astype(str)
    .str.replace(r'[^\d.]', '', regex=True)
)

df['gia'] = pd.to_numeric(df['gia'], errors='coerce')

# ==============================
# 5. XỬ LÝ LỖI DỮ LIỆU
# ==============================

# Đếm đơn lỗi
loi_data = df[
    df['ngay_dat'].isna() |
    df['gia'].isna()
]

so_don_loi = len(loi_data)

# Loại bỏ dòng lỗi
df = df.dropna(subset=['ngay_dat', 'gia'])

# ==============================
# 6. TẠO THÁNG
# ==============================

df['thang'] = df['ngay_dat'].dt.to_period('M')

# ==============================
# 7. BÁO CÁO
# ==============================

# Doanh thu theo tháng
doanhthu_thang = df.groupby('thang').agg(
    DoanhThu=('gia', 'sum')
).reset_index()

# Top 5 sản phẩm
top5_sp = df.groupby('ten_sp').agg(
    DoanhThu=('gia', 'sum')
).sort_values(by='DoanhThu', ascending=False).head(5).reset_index()

# ==============================
# 8. HIỂN THỊ
# ==============================

print("\n=== Doanh thu theo tháng ===")
print(doanhthu_thang)

print("\n=== Top 5 sản phẩm ===")
print(top5_sp)

print("\n=== Số đơn lỗi dữ liệu ===")
print(so_don_loi)

# ==============================
# 9. LƯU FILE
# ==============================

df.to_csv("banhang_clean.csv", index=False)
doanhthu_thang.to_csv("doanhthu_thang.csv", index=False)
top5_sp.to_csv("top5_sanpham.csv", index=False)

print("\n✔ Đã lưu file banhang_clean.csv")
print("✔ Đã lưu file doanhthu_thang.csv")
print("✔ Đã lưu file top5_sanpham.csv")