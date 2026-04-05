# Import thư viện pandas để xử lý dữ liệu bảng
import pandas as pd

# Đọc dữ liệu từ file CSV vào DataFrame
df = pd.read_csv("diem_sinhvien.csv")

# Tạo cột DiemTB theo công thức: 0.4 * DiemQT + 0.6 * DiemThi
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

# Định nghĩa hàm xếp loại dựa vào điểm trung bình
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"         # >= 8.5 → Giỏi
    elif diem >= 7.0:
        return "Kha"          # >= 7 → Khá
    elif diem >= 5.5:
        return "Trung binh"   # >= 5.5 → Trung bình
    else:
        return "Yeu"          # còn lại → Yếu

# Áp dụng hàm xếp loại cho cột DiemTB để tạo cột mới XepLoai
df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# Lọc ra các sinh viên có điểm trung bình >= 8
print("Sinh viên có DiemTB >= 8:")
print(df[df["DiemTB"] >= 8])

# Đổi tên cột HoTen thành TenSinhVien
df = df.rename(columns={"HoTen": "TenSinhVien"})

# Đặt cột MaSV làm chỉ mục (index)
df = df.set_index("MaSV")

# In ra DataFrame sau khi xử lý
print("\nDataFrame sau khi xử lý:")
print(df)