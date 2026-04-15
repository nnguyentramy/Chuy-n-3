import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("=== START ===")

# ================================
# 1. Đọc dữ liệu
# ================================
df = pd.read_csv("student_performance_dirty.csv")

print("Dữ liệu ban đầu:", len(df))

# ================================
# 2. Làm sạch dữ liệu
# ================================

# Xóa trùng
df = df.drop_duplicates()

# Giữ score hợp lệ (0-10)
df = df[(df["score_python"] >= 0) & (df["score_python"] <= 10)]

# Xóa dòng thiếu dữ liệu quan trọng
df = df.dropna(subset=["attendance_rate", "score_python"])

print("Sau khi làm sạch:", len(df))

# 👉 DEBUG QUAN TRỌNG
print(df[["score_python", "attendance_rate"]])

# ================================
# 3. Tạo label
# ================================
df["Label"] = df["score_python"].apply(lambda x: 1 if x >= 7 else 0)

# ================================
# 4. Feature
# ================================
X = df[["attendance_rate"]]
y = df["Label"]

# ================================
# 5. Train/Test
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ================================
# 6. CHƯA chuẩn hóa
# ================================
model_raw = LogisticRegression()
model_raw.fit(X_train, y_train)

pred_raw = model_raw.predict(X_test)

print("\nAccuracy chưa chuẩn hóa:",
      accuracy_score(y_test, pred_raw))

# ================================
# 7. Chuẩn hóa
# ================================
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ================================
# 8. SAU chuẩn hóa
# ================================
model_scaled = LogisticRegression()
model_scaled.fit(X_train_scaled, y_train)

pred_scaled = model_scaled.predict(X_test)

print("Accuracy sau chuẩn hóa:",
      accuracy_score(y_test, pred_scaled))

print("=== END ===")