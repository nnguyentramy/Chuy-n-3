import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("lienhe.csv")

print("=== Dữ liệu ban đầu ===")
print(df.head())

# 2. Chuẩn hóa email về chữ thường
df['Email'] = df['Email'].astype(str).str.strip().str.lower()

# 3. Kiểm tra email hợp lệ (regex)
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
df['Email_HopLe'] = df['Email'].str.contains(email_pattern, regex=True, na=False)

# 4. Tách mã vùng / đầu số điện thoại (3 số đầu)
df['SoDienThoai'] = df['SoDienThoai'].astype(str).str.strip()
df['DauSo'] = df['SoDienThoai'].str.extract(r'^(\d{3})')

# 5. Xóa khoảng trắng thừa trong địa chỉ
df['DiaChi'] = df['DiaChi'].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)

# 6. Trích xuất domain từ email
df['Domain'] = df['Email'].str.extract(r'@([\w\.-]+)')

# 7. Hiển thị kết quả
print("\n=== Dữ liệu sau khi làm sạch ===")
print(df)

# 8. Lưu file
df.to_csv("lienhe_clean.csv", index=False)

print("\n✔ Đã lưu file lienhe_clean.csv")