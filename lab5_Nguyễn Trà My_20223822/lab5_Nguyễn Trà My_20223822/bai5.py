import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# 1. Tạo 100 bước ngẫu nhiên
steps = np.random.choice([-1, 1], size=100)

# 2. Tính vị trí sau mỗi bước
walk = np.cumsum(steps)

# 3. In 10 giá trị đầu tiên
print("10 vị trí đầu tiên:", walk[:10])

# 5. Thông tin quan trọng
print("Vị trí cuối cùng:", walk[-1])
print("Vị trí lớn nhất:", np.max(walk))
print("Vị trí nhỏ nhất:", np.min(walk))

# 4. Vẽ đồ thị
plt.plot(walk)
plt.title("Random Walk 1 chiều")
plt.xlabel("Bước")
plt.ylabel("Vị trí")
plt.grid(True)
plt.show()