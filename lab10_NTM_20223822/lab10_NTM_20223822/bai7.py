import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# =========================
# Chuyển kiểu ngày tháng
# =========================
df["birth_date"] = pd.to_datetime(
    df["birth_date"],
    errors="coerce",   # lỗi sẽ thành NaT
    dayfirst=True      # ưu tiên ngày trước (dd-mm-yyyy)
)

# =========================
# Kiểm tra giá trị lỗi
# =========================
print("=== Số giá trị không chuyển đổi được ===")
print(df["birth_date"].isna().sum())

print("\n=== Các dòng bị lỗi ===")
print(df[df["birth_date"].isna()][["student_id", "birth_date"]])

# =========================
# Kiểm tra kiểu dữ liệu
# =========================
print("\n=== Kiểu dữ liệu ===")
print(df.dtypes)

print("\n=== 5 dòng dữ liệu ===")
print(df.head())