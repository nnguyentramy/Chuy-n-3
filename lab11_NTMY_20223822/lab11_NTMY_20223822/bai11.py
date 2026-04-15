import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ================================
# 1. Đọc và làm sạch dữ liệu
# ================================
df = pd.read_csv("student_performance_dirty.csv")

# Xóa trùng
df = df.drop_duplicates()

# Làm sạch dữ liệu điểm
df = df[(df["score_python"] >= 0) & (df["score_python"] <= 10)]

# Xử lý thiếu
df = df.dropna(subset=["attendance_rate", "score_python"])

# ================================
# 2. Chọn cột số
# ================================
df_num = df.select_dtypes(include=np.number)

print("=== Các cột số ===")
print(df_num.columns)

# ================================
# 3. Tính ma trận tương quan
# ================================
corr = df_num.corr()

print("\n=== Ma trận tương quan ===")
print(corr)

# ================================
# 4. Vẽ heatmap tương quan
# ================================
plt.figure()

plt.imshow(corr, interpolation='nearest')
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Ma trận tương quan")

plt.tight_layout()
plt.show()

# ================================
# 5. Tìm biến liên quan mạnh với target
# ================================
target_corr = corr["score_python"].sort_values(ascending=False)

print("\n=== Tương quan với score_python ===")
print(target_corr)