import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("sanpham.csv")

# 2. Hiển thị dữ liệu ban đầu
print("=== Dữ liệu ban đầu ===")
print(df.head())

# 3. Làm sạch cột Gia (xóa ký tự tiền tệ, dấu phẩy)
df['Gia'] = df['Gia'].astype(str).str.replace(r'[^\d.]', '', regex=True)

# 4. Chuyển Gia sang kiểu số
df['Gia'] = df['Gia'].astype(float)

# 5. Chuẩn hóa DanhMuc về chữ thường
df['DanhMuc'] = df['DanhMuc'].str.strip().str.lower()

# 6. Loại bỏ sản phẩm có số lượng tồn < 0
df = df[df['SoLuongTon'] >= 0]

# 7. Sắp xếp theo giá giảm dần
df = df.sort_values(by='Gia', ascending=False)

# 8. Kết quả sau xử lý
print("\n=== Dữ liệu sau khi làm sạch ===")
print(df)

# 9. Lưu file
df.to_csv("sanpham_clean.csv", index=False)

print("\n✔ Đã lưu file sanpham_clean.csv")