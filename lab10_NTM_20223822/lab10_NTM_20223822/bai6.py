import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# =========================
# Chuẩn hóa họ tên
# =========================
df["full_name"] = (
    df["full_name"]
    .str.replace(r"\s+", " ", regex=True)   # bỏ khoảng trắng dư
    .str.strip()                            # xóa khoảng trắng đầu/cuối
    .str.title()                            # viết hoa chữ cái đầu
)

# =========================
# Kiểm tra email hợp lệ
# =========================
email_mask = df["email"].str.contains(
    r"^[\w\.-]+@[\w\.-]+\.\w+$",
    regex=True,
    na=False
)

print("=== Email không hợp lệ ===")
print(df.loc[~email_mask, ["student_id", "email"]])

# =========================
# Chuẩn hóa số điện thoại
# =========================
df["phone"] = (
    df["phone"]
    .astype("string")
    .str.replace(r"\D", "", regex=True)     # chỉ giữ lại số
)

# =========================
# Kiểm tra kết quả
# =========================
print("\n=== 5 dòng dữ liệu sau khi xử lý ===")
print(df[["full_name", "email", "phone"]].head())