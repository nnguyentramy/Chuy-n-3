import numpy as np

scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])
# 1. In ma trận
print("Ma trận điểm:\n", scores)
# 2. Trung bình toàn bộ
print("Điểm trung bình toàn bộ:", np.mean(scores))
# 3. Trung bình từng sinh viên
avg_students = np.mean(scores, axis=1)
print("Điểm trung bình từng sinh viên:", avg_students)
# 4. Trung bình từng môn
avg_subjects = np.mean(scores, axis=0)
print("Điểm trung bình từng môn:", avg_subjects)
# 5. Max và Min
print("Điểm cao nhất:", np.max(scores))
print("Điểm thấp nhất:", np.min(scores))
# 6. Độ lệch chuẩn từng môn
print("Độ lệch chuẩn từng môn:", np.std(scores, axis=0))
# 7. Sinh viên có điểm TB cao nhất
best_student = np.argmax(avg_students)
print("Sinh viên có điểm TB cao nhất là vị trí:", best_student)