import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# Xóa trùng
df = df.drop_duplicates()

# Vẽ boxplot (chưa lọc để thấy ngoại lệ)
df.boxplot(column="score_python")

plt.title("Boxplot phát hiện ngoại lệ điểm Python")
plt.ylabel("Điểm")
plt.show()