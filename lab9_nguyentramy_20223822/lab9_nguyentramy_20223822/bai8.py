import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("chitieu.csv")

# 2. Hiển thị dữ liệu ban đầu
print("=== Dữ liệu ban đầu ===")
print(df.head())

# 3. Kiểm tra giao dịch không hợp lệ (SoTien <= 0)
invalid = df[df['SoTien'] <= 0]
print("\n=== Giao dịch không hợp lệ ===")
print(invalid)

# 4. Loại bỏ dữ liệu không hợp lệ
df = df[df['SoTien'] > 0]

# 5. Phân nhóm mức chi tiêu
bins = [0, 1000000, 5000000, float('inf')]
labels = ['Thấp', 'Trung bình', 'Cao']

df['MucChiTieu'] = pd.cut(df['SoTien'], bins=bins, labels=labels)

# 6. Thống kê số giao dịch theo từng mức
print("\n=== Số giao dịch theo mức chi tiêu ===")
print(df['MucChiTieu'].value_counts())

# 7. Tổng chi tiêu theo nhóm
tong_chi = df.groupby('NhomChiTieu')['SoTien'].agg('sum')

print("\n=== Tổng chi tiêu theo nhóm ===")
print(tong_chi)

# 8. Kết quả sau xử lý
print("\n=== Dữ liệu sau khi xử lý ===")
print(df.head())

# 9. Lưu file
df.to_csv("chitieu_clean.csv", index=False)

print("\n✔ Đã lưu file chitieu_clean.csv")