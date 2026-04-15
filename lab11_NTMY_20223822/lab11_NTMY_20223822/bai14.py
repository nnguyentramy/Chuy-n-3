import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

print("=== START ===")

# ================================
# 1. Đọc dữ liệu
# ================================
df = pd.read_csv("student_performance_dirty.csv")

print("Số dòng ban đầu:", len(df))

# ================================
# 2. Làm sạch dữ liệu
# ================================

# Xóa trùng
df = df.drop_duplicates()

# Làm sạch điểm (0-10)
df = df[(df["score_python"] >= 0) & (df["score_python"] <= 10)]

# Xóa dữ liệu thiếu
df = df.dropna(subset=["attendance_rate", "score_python"])

print("Sau khi làm sạch:", len(df))

# ================================
# 3. Tạo label (phân loại)
# ================================
df["Label"] = df["score_python"].apply(lambda x: 1 if x >= 7 else 0)

# Kiểm tra phân bố lớp
print("\nPhân bố Label:")
print(df["Label"].value_counts())

# Nếu chỉ có 1 lớp thì dừng
if df["Label"].nunique() < 2:
    print("❌ Dữ liệu chỉ có 1 lớp → không thể train!")
    exit()

# ================================
# 4. Feature (cải tiến thêm biến)
# ================================
X = df[["attendance_rate", "score_python"]]   # 🔥 dùng 2 biến cho tốt hơn
y = df["Label"]

# ================================
# 5. Train/Test (có stratify)
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y   # 🔥 đảm bảo đủ class
)

print("\nTrain:", len(X_train), "| Test:", len(X_test))

# ================================
# 6. Huấn luyện model (fix lệch lớp)
# ================================
model = LogisticRegression(
    max_iter=1000,
    class_weight='balanced'   # 🔥 tránh bias
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# ================================
# 7. Confusion Matrix
# ================================
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

print("\n=== Confusion Matrix ===")
print(cm)

# ================================
# 8. Classification Report
# ================================
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, labels=[0, 1], zero_division=0))

# ================================
# 9. Accuracy
# ================================
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\n=== END ===")