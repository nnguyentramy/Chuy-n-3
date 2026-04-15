import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# Làm sạch cơ bản
df = df.drop_duplicates()

# Lọc điểm hợp lệ (0 → 10)
df = df[(df["score_python"] >= 0) & (df["score_python"] <= 10)]

# Vẽ histogram
df["score_python"].plot(kind="hist", bins=5)
plt.title("Phân phối điểm Python")
plt.xlabel("Điểm")
plt.ylabel("Tần suất")
plt.show()