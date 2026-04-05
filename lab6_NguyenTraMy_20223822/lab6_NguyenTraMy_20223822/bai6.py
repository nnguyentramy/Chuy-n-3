# Import thư viện pandas để xử lý dữ liệu
import pandas as pd

# Đọc file CSV vào DataFrame
df = pd.read_csv("diem_sinhvien.csv")

# Hiển thị thông tin tổng quan dữ liệu
print("Thong tin du lieu:")
print(df.info())

# Tính cột điểm trung bình (DiemTB)
# Công thức: 40% điểm quá trình + 60% điểm thi
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

# Hàm xếp loại sinh viên dựa vào điểm trung bình
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"         # >= 8.5 → Giỏi
    elif diem >= 7.0:
        return "Kha"          # >= 7 → Khá
    elif diem >= 5.5:
        return "Trung binh"   # >= 5.5 → Trung bình
    else:
        return "Yeu"          # còn lại → Yếu

# Áp dụng hàm để tạo cột XepLoai
df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# Lọc sinh viên có xếp loại Giỏi hoặc Khá
ket_qua = df[df["XepLoai"].isin(["Gioi", "Kha"])]

# Sắp xếp theo DiemTB giảm dần
ket_qua = ket_qua.sort_values(by="DiemTB", ascending=False)

# Lưu kết quả ra file CSV mới
# index=False → không lưu cột index
# encoding="utf-8-sig" → tránh lỗi font tiếng Việt khi mở bằng Excel
ket_qua.to_csv("ketqua_xuly.csv", index=False, encoding="utf-8-sig")

# In kết quả ra màn hình
print("\nDanh sach sinh vien dat Kha tro len:")
print(ket_qua)

# Thông báo đã lưu file
print("\nDa luu file ketqua_xuly.csv")