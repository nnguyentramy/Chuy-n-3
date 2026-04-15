import pandas as pd
import numpy as np

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# =========================
# Phát hiện điểm không hợp lệ
# =========================
invalid_score = ~df["score_python"].between(0, 10)

print("=== Các giá trị điểm không hợp lệ ===")
print(df.loc[invalid_score, ["student_id", "score_python"]])

# =========================
# Gán NaN cho giá trị sai
# =========================
df.loc[invalid_score, "score_python"] = np.nan

# =========================
# Điền lại bằng median
# =========================
median_score = df["score_python"].median()
df["score_python"] = df["score_python"].fillna(median_score)

# =========================
# Kiểm tra lại
# =========================
print("\n=== Sau khi xử lý ===")
print(df["score_python"].describe())

print("\n=== 5 dòng dữ liệu ===")
print(df.head())