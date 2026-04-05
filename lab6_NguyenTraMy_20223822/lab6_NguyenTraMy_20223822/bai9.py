# Import thư viện pandas
import pandas as pd

# Tạo dữ liệu khách hàng (ít nhất 8 khách)
data = {
    "MaKH": ["KH01","KH02","KH03","KH04","KH05","KH06","KH07","KH08"],
    "TenKH": ["Lan","Minh","Hung","Ha","Phuong","Toan","Ngoc","Tuan"],
    "SoDonHang": [12, 5, 8, 15, 4, 10, 6, 3],  # số đơn hàng đã mua
    "TongChiTieu": [25000000, 7200000, 12500000, 31000000, 4300000, 9800000, 15000000, 2800000]  # tổng chi tiêu
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Hàm xếp loại khách hàng theo tổng chi tiêu
def xep_loai(tien):
    if tien >= 20000000:
        return "VIP"          # >= 20 triệu → VIP
    elif tien >= 10000000:
        return "Than thiet"   # >= 10 triệu → Thân thiết
    elif tien >= 5000000:
        return "Tiem nang"    # >= 5 triệu → Tiềm năng
    else:
        return "Thuong"       # còn lại → Thường

# Áp dụng hàm để tạo cột XepLoaiKH
df["XepLoaiKH"] = df["TongChiTieu"].apply(xep_loai)

# Lọc danh sách khách hàng VIP và Thân thiết
print("Danh sach khach hang VIP va Than thiet:")
print(df[df["XepLoaiKH"].isin(["VIP", "Than thiet"])])

# Sắp xếp danh sách khách hàng theo TongChiTieu giảm dần
print("\nDanh sach khach hang sap xep theo TongChiTieu giam dan:")
print(df.sort_values(by="TongChiTieu", ascending=False))

# Tính mức chi tiêu trung bình của khách hàng
muc_chi_tieu_tb = df["TongChiTieu"].mean()
print("\nChi tieu trung binh:", muc_chi_tieu_tb)