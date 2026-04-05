# Import thư viện pandas để làm việc với dữ liệu dạng bảng
import pandas as pd

# Tạo dữ liệu dạng dict (mỗi key là 1 cột)
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05"],  # mã sinh viên
    "HoTen": ["An", "Bình", "Chi", "Dũng", "Hà"],     # họ tên
    "Lop": ["CNTT1", "CNTT1", "CNTT2", "CNTT2", "CNTT1"],  # lớp
    "DiemQT": [7.0, 8.5, 6.0, 9.0, 8.0],   # điểm quá trình
    "DiemThi": [7.5, 8.0, 6.5, 9.5, 8.5]   # điểm thi
}

# Tạo DataFrame từ dict
df = pd.DataFrame(data)

# Hiển thị toàn bộ DataFrame
print("Danh sách sinh viên:")
print(df)

# Chọn riêng 2 cột HoTen và DiemThi
print("\nChọn cột HoTen và DiemThi:")
print(df[["HoTen", "DiemThi"]])

# Tạo cột mới DiemTB theo công thức: 0.4 * DiemQT + 0.6 * DiemThi
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

# In lại DataFrame sau khi thêm cột mới
print("\nDataFrame sau khi thêm cột DiemTB:")
print(df)