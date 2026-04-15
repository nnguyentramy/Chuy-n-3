# 1. Import
import pandas as pd
import numpy as np
import re
from datetime import datetime

# 2. Đọc dữ liệu
df = pd.read_csv("student_performance_dirty.csv")

# 3. Hàm clean

def clean_gender(series):
    return (series.astype("string")
            .str.strip()
            .str.lower()
            .replace({
                "nam": "Nam",
                "nữ": "Nữ",
                "nu": "Nữ"
            })
            .fillna("Không rõ"))

def clean_phone(series):
    return (series.astype("string")
            .str.replace(r"\D", "", regex=True)
            .replace("", "Chưa cập nhật")
            .fillna("Chưa cập nhật"))

# 4. Áp dụng
df["gender"] = clean_gender(df["gender"])
df["phone"] = clean_phone(df["phone"])

# 5. Tạo age
df["birth_date"] = pd.to_datetime(df["birth_date"], errors="coerce")
current_year = datetime.now().year
df["age"] = current_year - df["birth_date"].dt.year

# 6. Tách họ tên
df["full_name"] = df["full_name"].str.strip()
name_split = df["full_name"].str.split(" ", expand=True)

df["last_name"] = name_split[0]
df["first_name"] = name_split[name_split.columns[-1]]
df["middle_name"] = name_split.iloc[:,1:-1].apply(
    lambda x: " ".join(x.dropna()), axis=1
)

# 7. So sánh fillna
df_mean = df.copy()
df_mean["score_python"] = df_mean["score_python"].fillna(df_mean["score_python"].mean())

df_median = df.copy()
df_median["score_python"] = df_median["score_python"].fillna(df_median["score_python"].median())

# 8. Lưu file
df.to_csv("student_clean.csv", index=False, encoding="utf-8-sig")

print("Đã chạy xong!")