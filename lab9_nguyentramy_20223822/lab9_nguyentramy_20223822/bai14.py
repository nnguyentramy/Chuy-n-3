import pandas as pd

# ==============================
# 1. ĐỌC DỮ LIỆU
# ==============================
df = pd.read_csv("reviews.csv")

print("=== Dữ liệu ban đầu ===")
print(df.head())

# ==============================
# 2. XÓA TRÙNG LẶP
# ==============================
df = df.drop_duplicates(subset='ReviewID')

# ==============================
# 3. XỬ LÝ RATING
# ==============================
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Ép về khoảng 1–5
df['Rating'] = df['Rating'].clip(1, 5)

# ==============================
# 4. LÀM SẠCH COMMENT
# ==============================
df['Comment'] = (
    df['Comment']
    .astype(str)
    .str.strip()
    .str.replace(r'\s+', ' ', regex=True)        # xóa khoảng trắng dư
    .str.replace(r'(.)\1{2,}', r'\1\1', regex=True)  # ký tự lặp (vd: gooooood → good)
)

# ==============================
# 5. ĐỘ DÀI BÌNH LUẬN
# ==============================
df['CommentLength'] = df['Comment'].str.len()

# ==============================
# 6. CHUẨN HÓA DANH MỤC
# ==============================
df['ProductCategory'] = (
    df['ProductCategory']
    .astype(str)
    .str.strip()
    .str.lower()
)

# ==============================
# 7. CHUẨN HÓA NGÀY
# ==============================
df['ReviewDate'] = pd.to_datetime(df['ReviewDate'], errors='coerce')

# ==============================
# 8. THỐNG KÊ
# ==============================
thongke = df.groupby('ProductCategory').agg(
    SoReview=('ReviewID', 'count'),
    RatingTB=('Rating', 'mean')
).reset_index()

# ==============================
# 9. HIỂN THỊ
# ==============================
print("\n=== Dữ liệu sau khi làm sạch ===")
print(df.head())

print("\n=== Thống kê theo danh mục ===")
print(thongke)

# ==============================
# 10. LƯU FILE
# ==============================
df.to_csv("reviews_clean.csv", index=False)
thongke.to_csv("reviews_thongke.csv", index=False)

print("\n✔ Đã lưu reviews_clean.csv")
print("✔ Đã lưu reviews_thongke.csv")