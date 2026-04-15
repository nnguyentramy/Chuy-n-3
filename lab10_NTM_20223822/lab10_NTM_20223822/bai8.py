import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# =========================
# Phân nhóm điểm
# =========================
bins = [0, 5, 6.5, 8, 10]
labels = ["Yếu", "Trung bình", "Khá", "Giỏi"]

df["level"] = pd.cut(
    df["score_python"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# =========================
# Kiểm tra kết quả
# =========================
print("=== 5 dòng dữ liệu ===")
print(df[["student_id", "score_python", "level"]].head())

print("\n=== Thống kê số lượng mỗi nhóm ===")
print(df["level"].value_counts())