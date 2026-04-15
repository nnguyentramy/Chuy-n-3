import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# =========================
# Chuẩn hóa cột class_name
# =========================
df["class_name"] = (
    df["class_name"]
    .str.replace("-", " ", regex=False)      # CNTT-3 -> CNTT 3
    .str.replace(r"\s+", " ", regex=True)    # bỏ khoảng trắng dư
    .str.strip()                             # xóa khoảng trắng đầu/cuối
    .str.upper()                             # viết hoa
    .replace({
        "CNTT1": "CNTT 1",
        "CNTT2": "CNTT 2",
        "CNTT3": "CNTT 3"
    })
)

# =========================
# Chuẩn hóa cột gender
# =========================
df["gender"] = (
    df["gender"]
    .astype("string")                        # tránh lỗi None
    .str.strip()                             # xóa khoảng trắng
    .str.lower()                             # chuyển về chữ thường
    .replace({
        "nam": "Nam",
        "nữ": "Nữ",
        "nu": "Nữ"
    })
)

# =========================
# Kiểm tra kết quả
# =========================
print("=== class_name sau khi chuẩn hóa ===")
print(df["class_name"].unique())

print("\n=== gender sau khi chuẩn hóa ===")
print(df["gender"].unique())

print("\n=== 5 dòng dữ liệu ===")
print(df.head())