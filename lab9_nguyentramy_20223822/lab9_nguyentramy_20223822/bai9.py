import pandas as pd
import matplotlib.pyplot as plt

# 1. Đọc dữ liệu
df = pd.read_csv("moitruong.csv")

# 2. Ép kiểu float để tránh warning
df['NhietDo'] = df['NhietDo'].astype(float)

print("=== Dữ liệu ban đầu ===")
print(df.head())

# 3. Tính IQR
Q1 = df['NhietDo'].quantile(0.25)
Q3 = df['NhietDo'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# 4. Đánh dấu outlier
df['Outlier'] = (df['NhietDo'] < lower) | (df['NhietDo'] > upper)

print("\n=== Số lượng ngoại lệ ===")
print(df['Outlier'].value_counts())

# 5. Thống kê trước
print("\n=== Thống kê trước xử lý ===")
print(df['NhietDo'].describe())

# 6. Thay bằng median
median = df['NhietDo'].median()
df.loc[df['Outlier'], 'NhietDo'] = median

# 7. Thống kê sau
print("\n=== Thống kê sau xử lý ===")
print(df['NhietDo'].describe())

# 8. Vẽ boxplot
plt.figure()
df.boxplot(column='NhietDo')
plt.title("Boxplot NhietDo sau khi xử lý")
plt.show()

# 9. Lưu file
df.to_csv("moitruong_clean.csv", index=False)

print("\n✔ Đã lưu file moitruong_clean.csv")