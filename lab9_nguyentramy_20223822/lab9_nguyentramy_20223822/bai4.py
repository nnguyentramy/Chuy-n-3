import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("muonsach.csv")

# 2. Hiển thị dữ liệu ban đầu
print("=== Dữ liệu ban đầu ===")
print(df.head())

# 3. Chuyển kiểu ngày tháng
df['NgayMuon'] = pd.to_datetime(df['NgayMuon'])
df['NgayTra'] = pd.to_datetime(df['NgayTra'])

# 4. Chuẩn hóa TrangThai
df['TrangThai'] = df['TrangThai'].str.strip().str.lower()

df['TrangThai'] = df['TrangThai'].replace({
    'đã trả': 'DaTra',
    'da tra': 'DaTra',
    'datra': 'DaTra',
    'chưa trả': 'ChuaTra',
    'chua tra': 'ChuaTra',
    'chuatra': 'ChuaTra'
})

# 5. Tính số ngày mượn
# Nếu chưa trả thì dùng ngày hiện tại
df['NgayTra_temp'] = df['NgayTra'].fillna(pd.Timestamp.today())

df['SoNgayMuon'] = (df['NgayTra_temp'] - df['NgayMuon']).dt.days

# Xóa cột tạm
df = df.drop(columns=['NgayTra_temp'])

# 6. Lọc sinh viên mượn quá 30 ngày và chưa trả
qua_han = df[(df['SoNgayMuon'] > 30) & (df['NgayTra'].isna())]

print("\n=== Sinh viên mượn quá 30 ngày ===")
print(qua_han)

# 7. Kết quả sau xử lý
print("\n=== Dữ liệu sau khi làm sạch ===")
print(df.head())

# 8. Lưu file
df.to_csv("muonsach_clean.csv", index=False)

print("\n✔ Đã lưu file muonsach_clean.csv")