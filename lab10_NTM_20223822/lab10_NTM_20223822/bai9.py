import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# =========================
# Tính IQR
# =========================
q1 = df["attendance_rate"].quantile(0.25)
q3 = df["attendance_rate"].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print("Ngưỡng dưới:", lower)
print("Ngưỡng trên:", upper)

# =========================
# Lọc outlier
# =========================
outlier_df = df[
    (df["attendance_rate"] < lower) |
    (df["attendance_rate"] > upper)
]

print("\n=== Các bản ghi nghi ngờ ===")
print(outlier_df[["student_id", "attendance_rate"]])

# =========================
# Lưu danh sách outlier
# =========================
outlier_df.to_csv("attendance_outliers.csv", index=False, encoding="utf-8-sig")