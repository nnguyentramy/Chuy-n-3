import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# 2. Làm sạch dữ liệu
df = df.drop_duplicates()
df = df.dropna(subset=["attendance_rate", "score_python"])

# Lọc điểm hợp lệ
df = df[(df["score_python"] >= 0) & (df["score_python"] <= 10)]

# 3. Tạo nhãn
df["Label"] = df["score_python"].apply(lambda x: 1 if x >= 7 else 0)

print("Phân bố nhãn:")
print(df["Label"].value_counts())

# 4. Chọn nhiều biến đầu vào hơn (cải thiện model)
X = df[["attendance_rate", "score_python"]]
y = df["Label"]

# 5. Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 6. Huấn luyện mô hình
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 7. Dự đoán
y_pred = model.predict(X_test)

# 8. Đánh giá
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 9. So sánh kết quả
print("\nSo sánh dự đoán:")
for real, pred in zip(y_test, y_pred):
    print(f"Thực tế: {real} | Dự đoán: {pred}")