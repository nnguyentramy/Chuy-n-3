# Import thư viện pandas
import pandas as pd

# Tạo dữ liệu hóa đơn bán hàng (ít nhất 10 hóa đơn)
data = {
    "MaHD": ["HD01","HD02","HD03","HD04","HD05","HD06","HD07","HD08","HD09","HD10"],
    "NgayBan": ["2026-04-01","2026-04-01","2026-04-02","2026-04-02","2026-04-03",
                "2026-04-03","2026-04-04","2026-04-04","2026-04-05","2026-04-05"],
    "TenSP": ["Laptop","Chuot","Man hinh","USB","Loa","Tai nghe","Laptop","Webcam","Ban phim","Man hinh"],
    "SoLuong": [1, 5, 2, 10, 3, 4, 1, 2, 6, 1],   # số lượng bán
    "DonGia": [14500000,150000,2500000,180000,750000,450000,14500000,900000,300000,2500000],  # giá
    "NhanVien": ["An","Binh","An","Chi","Dung","Ha","An","Chi","Binh","Ha"]  # nhân viên bán
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Tạo cột ThanhTien = SoLuong * DonGia
df["ThanhTien"] = df["SoLuong"] * df["DonGia"]

# Hiển thị 5 hóa đơn có giá trị cao nhất
print("5 hoa don co gia tri cao nhat:")
print(df.sort_values(by="ThanhTien", ascending=False).head(5))

# Lọc các hóa đơn có ThanhTien >= 3.000.000
print("\nHoa don co ThanhTien >= 3000000:")
print(df[df["ThanhTien"] >= 3000000])

# Tính tổng doanh thu toàn bộ bảng dữ liệu
tong_doanh_thu = df["ThanhTien"].sum()
print("\nTong doanh thu:", tong_doanh_thu)