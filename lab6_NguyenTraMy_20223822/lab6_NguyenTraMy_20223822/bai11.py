# Import thư viện pandas
import pandas as pd

# Tạo dữ liệu kho gồm ít nhất 6 sản phẩm
data = {
    "MaSP": ["SP01","SP02","SP03","SP04","SP05","SP06"],
    "TenSP": ["Laptop","Chuot","Ban phim","USB","Loa","Webcam"],
    "TonDau": [5, 20, 15, 30, 10, 8],      # tồn đầu kỳ
    "NhapThem": [3, 10, 5, 20, 4, 2],     # nhập thêm
    "DaBan": [4, 18, 12, 35, 9, 3],       # đã bán
    "DonGia": [14500000,150000,300000,180000,750000,900000]  # giá sản phẩm
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Tính cột TonCuoi = TonDau + NhapThem - DaBan
df["TonCuoi"] = df["TonDau"] + df["NhapThem"] - df["DaBan"]

# Tính cột GiaTriTonCuoi = TonCuoi * DonGia
df["GiaTriTonCuoi"] = df["TonCuoi"] * df["DonGia"]

# In toàn bộ bảng dữ liệu
print("Danh sach mat hang va ton kho:")
print(df)

# Lọc các sản phẩm sắp hết hàng (TonCuoi <= 5)
print("\nSan pham sap het hang:")
print(df[df["TonCuoi"] <= 5])

# Tìm sản phẩm có giá trị tồn cuối lớn nhất
print("\nSan pham co GiaTriTonCuoi lon nhat:")
print(df.loc[df["GiaTriTonCuoi"].idxmax()])