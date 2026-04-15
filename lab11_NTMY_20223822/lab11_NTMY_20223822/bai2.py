import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# Làm sạch nhanh (để vẽ cho đúng)
df = df.drop_duplicates()

# Chuẩn hóa class_name (đơn giản)
df['class_name'] = df['class_name'].str.replace("-", " ")
df['class_name'] = df['class_name'].str.replace("CNTT1", "CNTT 1")

# Nhóm dữ liệu và tính điểm trung bình
group_data = df.groupby("class_name")["score_python"].mean()

# Vẽ biểu đồ cột
group_data.plot(kind="bar")
plt.title("Điểm Python trung bình theo lớp")
plt.xlabel("Lớp")
plt.ylabel("Điểm trung bình")
plt.show()