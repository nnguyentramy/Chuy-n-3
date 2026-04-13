import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("suckhoe.csv")

# 2. Hiển thị dữ liệu ban đầu
print("=== Dữ liệu ban đầu ===")
print(df.head())

# 3. Phát hiện tuổi bất thường
tuoi_loi = df[(df['Tuoi'] <= 0) | (df['Tuoi'] > 100)]
print("\n=== Các dòng tuổi không hợp lệ ===")
print(tuoi_loi)

# 4. Kiểm tra thiếu dữ liệu
print("\n=== Giá trị thiếu ===")
print(df[['CanNang', 'ChieuCao']].isna().sum())

# 5. Điền giá trị thiếu bằng trung vị
df['CanNang'] = df['CanNang'].fillna(df['CanNang'].median())
df['ChieuCao'] = df['ChieuCao'].fillna(df['ChieuCao'].median())

# 6. Chuẩn hóa nhóm máu
df['NhomMau'] = df['NhomMau'].str.strip().str.upper()

df['NhomMau'] = df['NhomMau'].replace({
    'A+': 'A', 'A-': 'A',
    'B+': 'B', 'B-': 'B',
    'AB+': 'AB', 'AB-': 'AB',
    'O+': 'O', 'O-': 'O'
})

# 7. Tính BMI
df['BMI'] = df['CanNang'] / ((df['ChieuCao'] / 100) ** 2)

# 8. Kết quả sau xử lý
print("\n=== Dữ liệu sau khi xử lý ===")
print(df.head())

# 9. Lưu file
df.to_csv("suckhoe_clean.csv", index=False)

print("\n✔ Đã lưu file suckhoe_clean.csv")