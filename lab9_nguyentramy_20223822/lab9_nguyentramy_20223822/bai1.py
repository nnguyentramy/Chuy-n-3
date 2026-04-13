import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("diem_sinhvien.csv")

# 2. Hiển thị thông tin cơ bản
print("=== Thông tin dữ liệu ===")
print(df.info())

print("\n=== 5 dòng đầu ===")
print(df.head())

# 3. Kiểm tra giá trị thiếu
print("\n=== Giá trị thiếu ===")
print(df.isna().sum())

# 4. Xử lý dữ liệu thiếu (KHÔNG dùng inplace)
df['DiemQT'] = df['DiemQT'].fillna(df['DiemQT'].mean())
df['DiemThi'] = df['DiemThi'].fillna(df['DiemThi'].mean())
df['HoTen'] = df['HoTen'].fillna("ChuaCapNhat")

# 5. Tính lại DiemTK
df['DiemTK'] = 0.4 * df['DiemQT'] + 0.6 * df['DiemThi']

# 6. Xếp loại
def xep_loai(diem):
    if diem >= 8:
        return "A"
    elif diem >= 6.5:
        return "B"
    elif diem >= 5:
        return "C"
    else:
        return "D"

df['XepLoai'] = df['DiemTK'].apply(xep_loai)

# 7. Hiển thị kết quả
print("\n=== Dữ liệu sau khi làm sạch ===")
print(df)

# 8. Lưu file mới
df.to_csv("diem_sinhvien_clean.csv", index=False)

print("\n✔ Đã lưu file diem_sinhvien_clean.csv")