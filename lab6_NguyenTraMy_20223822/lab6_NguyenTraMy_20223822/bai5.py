# Import thư viện pandas
import pandas as pd

# Tạo dữ liệu khảo sát của 10 sinh viên
data = {
    "MaSV": ["SV01","SV02","SV03","SV04","SV05","SV06","SV07","SV08","SV09","SV10"],
    "GioTuHoc": [3, 2, 1, 4, 2.5, 1.5, 3.5, 2, 1, 4],   # số giờ tự học mỗi ngày
    "SoBuoiNghi": [1, 2, 4, 0, 1, 3, 0, 2, 5, 1],       # số buổi nghỉ học
    "DiemCC": [9, 8, 6, 10, 8, 6, 9, 8, 5, 10],         # điểm chuyên cần
    "DiemCuoiKy": [8, 7.5, 6, 9, 8, 6.5, 8.5, 7, 5.5, 9] # điểm cuối kỳ
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Tính điểm trung bình (DiemTB)
# Công thức: 30% chuyên cần + 70% cuối kỳ
df["DiemTB"] = 0.3 * df["DiemCC"] + 0.7 * df["DiemCuoiKy"]

# Hàm phân nhóm học tập
def nhom_hoc_tap(row):
    # Nếu tự học >= 3 giờ và nghỉ <= 1 → tích cực
    if row["GioTuHoc"] >= 3 and row["SoBuoiNghi"] <= 1:
        return "Tich cuc"
    # Nếu tự học >= 2 giờ và nghỉ <= 2 → bình thường
    elif row["GioTuHoc"] >= 2 and row["SoBuoiNghi"] <= 2:
        return "Binh thuong"
    # Còn lại → cần hỗ trợ
    else:
        return "Can ho tro"

# Áp dụng hàm cho từng dòng để tạo cột NhomHocTap
df["NhomHocTap"] = df.apply(nhom_hoc_tap, axis=1)

# In toàn bộ dữ liệu
print("Toan bo du lieu:")
print(df)

# Lọc sinh viên học > 2 giờ/ngày và nghỉ <= 2 buổi
print("\nSinh vien tu hoc > 2 gio va nghi <= 2 buoi:")
print(df[(df["GioTuHoc"] > 2) & (df["SoBuoiNghi"] <= 2)])