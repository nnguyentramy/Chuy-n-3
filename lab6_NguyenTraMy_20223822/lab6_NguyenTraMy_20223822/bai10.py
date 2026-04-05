# Import thư viện pandas
import pandas as pd

# Tạo dữ liệu 12 giao dịch bán hàng
data = {
    "MaHD": ["HD01","HD02","HD03","HD04","HD05","HD06","HD07","HD08","HD09","HD10","HD11","HD12"],
    "NhanVien": ["An","Binh","Chi","An","Dung","Chi","An","Binh","Dung","Chi","An","Binh"],
    "SoLuong": [1,5,2,3,1,4,2,6,1,2,1,3],  # số lượng bán
    "DonGia": [14500000,150000,2500000,750000,900000,450000,300000,180000,2500000,900000,14500000,300000]  # giá
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Tạo cột DoanhThu = SoLuong * DonGia
df["DoanhThu"] = df["SoLuong"] * df["DonGia"]

# Tính tổng doanh thu của từng nhân viên bằng groupby
tong_nv = df.groupby("NhanVien")["DoanhThu"].sum().reset_index()

# Sắp xếp theo DoanhThu giảm dần
tong_nv = tong_nv.sort_values(by="DoanhThu", ascending=False)

# In tổng doanh thu từng nhân viên
print("Tong doanh thu cua tung nhan vien:")
print(tong_nv)

# Xác định nhân viên có doanh thu cao nhất
print("\nNhan vien doanh thu cao nhat:")
print(tong_nv.iloc[0])

# Nhận xét ngắn về kết quả
print("\nNhan xet:")
for i, row in tong_nv.iterrows():
    print(f"- Nhan vien {row['NhanVien']}: Doanh thu {row['DoanhThu']:,} VND")