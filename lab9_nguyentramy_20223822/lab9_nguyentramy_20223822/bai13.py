import pandas as pd

# ==============================
# 1. ĐỌC DỮ LIỆU
# ==============================
df = pd.read_csv("benhnhan.csv")

print("=== Dữ liệu ban đầu ===")
print(df.head())

# ==============================
# 2. CHUẨN HÓA CỘT PHÂN LOẠI
# ==============================

# Giới tính
df['GioiTinh'] = (
    df['GioiTinh']
    .astype(str)
    .str.strip()
    .str.lower()
    .replace({
        'nam': 'Nam',
        'male': 'Nam',
        'nữ': 'Nu',
        'nu': 'Nu',
        'female': 'Nu'
    })
    .infer_objects(copy=False)
)

# Chẩn đoán
df['ChanDoan'] = df['ChanDoan'].astype(str).str.strip().str.title()

# ==============================
# 3. ÉP KIỂU SỐ
# ==============================

cols_num = ['Tuoi', 'HuyetApTamThu', 'HuyetApTamTruong', 'DuongHuyet']

for col in cols_num:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ==============================
# 4. XỬ LÝ GIÁ TRỊ THIẾU
# ==============================

# Số → median
for col in cols_num:
    df[col] = df[col].fillna(df[col].median())

# Phân loại → mode
df['GioiTinh'] = df['GioiTinh'].fillna(df['GioiTinh'].mode()[0])
df['ChanDoan'] = df['ChanDoan'].fillna(df['ChanDoan'].mode()[0])

# ==============================
# 5. PHÁT HIỆN & XỬ LÝ OUTLIER (IQR)
# ==============================

for col in cols_num:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # Thay outlier bằng median
    median = df[col].median()
    df.loc[(df[col] < lower) | (df[col] > upper), col] = median

# ==============================
# 6. MÃ HÓA CHẨN ĐOÁN
# ==============================

df['ChanDoan_Code'] = df['ChanDoan'].astype('category').cat.codes

# ==============================
# 7. CHUẨN HÓA (MIN-MAX SCALING)
# ==============================

for col in cols_num:
    min_val = df[col].min()
    max_val = df[col].max()
    df[col + '_Scaled'] = (df[col] - min_val) / (max_val - min_val)

# ==============================
# 8. HIỂN THỊ
# ==============================

print("\n=== Dữ liệu sau xử lý ===")
print(df.head())

# ==============================
# 9. LƯU FILE
# ==============================

df.to_csv("benhnhan_clean.csv", index=False)

print("\n✔ Đã lưu file benhnhan_clean.csv")