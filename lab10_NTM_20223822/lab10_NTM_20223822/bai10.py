import pandas as pd

# Đọc dữ liệu (giả sử đã xử lý các bước trước đó)
df = pd.read_csv("student_performance_dirty.csv")

# =========================
# (Ở bài thực tế: df này đã được xử lý qua các bước 1→9)
# =========================

# Lưu file sạch
df.to_csv("student_performance_clean.csv", index=False, encoding="utf-8-sig")

print("Đã lưu file student_performance_clean.csv")