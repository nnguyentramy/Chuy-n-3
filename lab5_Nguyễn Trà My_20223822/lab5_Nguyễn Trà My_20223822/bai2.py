import numpy as np

scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])
# 1. Trung bình từng môn
mean_col = np.mean(scores, axis=0)
# 2. Độ lệch chuẩn từng môn
std_col = np.std(scores, axis=0)
# 3. Chuẩn hóa Z-score (broadcasting)
z_scores = (scores - mean_col) / std_col
# 4. In kết quả làm tròn 2 chữ số
print("Ma trận sau chuẩn hóa (Z-score):")
print(np.round(z_scores, 2))
# 5. Kiểm tra trung bình các cột
print("TB các cột sau chuẩn hóa:", np.round(np.mean(z_scores, axis=0), 5))