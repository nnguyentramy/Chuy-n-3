import pandas as pd

# ==============================
# 1. ĐỌC DỮ LIỆU
# ==============================
df = pd.read_csv("ecommerce_full.csv")

print("=== Dữ liệu gốc ===")
print(df.head())

# ==============================
# 2. KHÁM PHÁ LỖI
# ==============================
print("\n=== Thông tin ===")
print(df.info())

print("\n=== Missing ===")
print(df.isnull().sum())

# ==============================
# 3. XỬ LÝ MISSING
# ==============================

# Số → median
num_cols = ['Price', 'Quantity']
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col] = df[col].fillna(df[col].median())

# Chuỗi → mode
df['Category'] = df['Category'].fillna(df['Category'].mode()[0])

# ==============================
# 4. XỬ LÝ TRÙNG
# ==============================
df = df.drop_duplicates()

# ==============================
# 5. CHUẨN HÓA DỮ LIỆU
# ==============================

# Category
df['Category'] = df['Category'].astype(str).str.strip().str.lower()

# Date
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')

# Text
df['ProductName'] = df['ProductName'].astype(str).str.strip()

# ==============================
# 6. XỬ LÝ OUTLIER (IQR)
# ==============================

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    median = df[col].median()
    df.loc[(df[col] < lower) | (df[col] > upper), col] = median

# ==============================
# 7. FEATURE ENGINEERING
# ==============================

# 1. Tổng tiền
df['TotalAmount'] = df['Price'] * df['Quantity']

# 2. Tháng
df['Month'] = df['OrderDate'].dt.month

# 3. Nhóm giá
df['PriceGroup'] = pd.qcut(df['Price'], q=3, labels=['Low', 'Medium', 'High'])

# ==============================
# 8. LƯU FILE
# ==============================

df.to_csv("ecommerce_clean.csv", index=False)

print("\n✔ Đã lưu ecommerce_clean.csv")
