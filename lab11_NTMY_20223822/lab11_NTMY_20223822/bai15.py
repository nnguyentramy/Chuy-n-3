# ================================
# 0. Import thư viện
# ================================
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("=== START PROJECT ===")

# ================================
# 1. Đọc dữ liệu
# ================================
df = pd.read_csv("student_performance_dirty.csv")

print("\n=== 1. Dữ liệu ban đầu ===")
print(df.head())
print("Số dòng:", len(df))

# ================================
# 2. Khám phá dữ liệu
# ================================
print("\n=== 2. Thông tin dữ liệu ===")
print(df.info())

print("\n=== Thống kê mô tả ===")
print(df.describe())

# ================================
# 3. Làm sạch dữ liệu
# ================================

# Xóa trùng
df = df.drop_duplicates()

# Làm sạch điểm
df = df[(df["score_python"] >= 0) & (df["score_python"] <= 10)]

# Xóa thiếu
df = df.dropna(subset=["attendance_rate", "score_python"])

print("\nSau khi làm sạch:", len(df))

# ================================
# 4. Trực quan hóa (4 biểu đồ)
# ================================

# Biểu đồ 1: Histogram điểm
plt.figure()
plt.hist(df["score_python"])
plt.title("Phân bố điểm Python")
plt.xlabel("Score")
plt.ylabel("Số lượng")
plt.show()

# Biểu đồ 2: Histogram chuyên cần
plt.figure()
plt.hist(df["attendance_rate"])
plt.title("Phân bố chuyên cần")
plt.xlabel("Attendance")
plt.ylabel("Số lượng")
plt.show()

# Biểu đồ 3: Scatter
plt.figure()
plt.scatter(df["attendance_rate"], df["score_python"])
plt.title("Attendance vs Score")
plt.xlabel("Attendance")
plt.ylabel("Score")
plt.show()

# Biểu đồ 4: Boxplot
plt.figure()
plt.boxplot(df["score_python"])
plt.title("Boxplot điểm Python")
plt.show()

# ================================
# 5. Xây dựng bài toán (Phân loại)
# ================================

# Tạo label
df["Label"] = df["score_python"].apply(lambda x: 1 if x >= 7 else 0)

# Feature
X = df[["attendance_rate", "score_python"]]
y = df["Label"]

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ================================
# 6. Huấn luyện mô hình
# ================================
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# ================================
# 7. Đánh giá mô hình
# ================================
print("\n=== Accuracy ===")
print(accuracy_score(y_test, y_pred))

print("\n=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred, labels=[0,1]))

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, zero_division=0))

print("\n=== END PROJECT ===")