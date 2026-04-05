# Import thư viện pandas để xử lý dữ liệu bảng
import pandas as pd

# Tạo dữ liệu sản phẩm (ít nhất 8 sản phẩm)
data = {
    "MaSP": ["SP01", "SP02", "SP03", "SP04", "SP05", "SP06", "SP07", "SP08"],
    "TenSP": ["Chuot", "Ban phim", "Man hinh", "USB", "Laptop", "Loa", "Tai nghe", "Webcam"],
    "LoaiHang": ["Phu kien", "Phu kien", "Thiet bi", "Phu kien", "Thiet bi", "Thiet bi", "Phu kien", "Thiet bi"],
    "DonGia": [150000, 300000, 2500000, 180000, 14500000, 750000, 450000, 900000],  # giá sản phẩm
    "SoLuongTon": [25, 18, 7, 40, 5, 12, 20, 8]  # số lượng tồn kho
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Tạo cột GiaTriTonKho = DonGia * SoLuongTon
df["GiaTriTonKho"] = df["DonGia"] * df["SoLuongTon"]

# In toàn bộ danh sách sản phẩm
print("Danh sach san pham:")
print(df)

# Lọc sản phẩm có đơn giá > 500000
print("\nSan pham co DonGia > 500000:")
print(df[df["DonGia"] > 500000])

# Sắp xếp sản phẩm theo GiaTriTonKho giảm dần
print("\nSan pham sap xep theo GiaTriTonKho giam dan:")
print(df.sort_values(by="GiaTriTonKho", ascending=False))

# Lọc sản phẩm có số lượng tồn < 10
print("\nSan pham co SoLuongTon < 10:")
print(df[df["SoLuongTon"] < 10])