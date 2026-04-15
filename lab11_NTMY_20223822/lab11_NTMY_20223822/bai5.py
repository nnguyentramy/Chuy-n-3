import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# Xóa trùng
df = df.drop_duplicates()

# Lọc dữ liệu hợp lệ
df = df[
    (df["score_python"] >= 0) & (df["score_python"] <= 10)
]

# Bỏ dòng bị thiếu
df = df.dropna(subset=["attendance_rate", "score_python"])

# Vẽ scatter plot
df.plot(kind="scatter", x="attendance_rate", y="score_python")

plt.title("Mối quan hệ giữa chuyên cần và điểm Python")
plt.xlabel("Tỷ lệ chuyên cần (%)")
plt.ylabel("Điểm Python")
plt.show()