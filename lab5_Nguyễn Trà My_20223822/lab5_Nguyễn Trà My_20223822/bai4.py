import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([
    [4, 2],
    [1, 5]
])

# 1. A + B
print("A + B =\n", A + B)

# 2. A - B
print("A - B =\n", A - B)

# 3. A @ B
print("A @ B =\n", A @ B)

# 4. Định thức A
det_A = np.linalg.det(A)
print("det(A) =", det_A)

# 5. Nghịch đảo A
inv_A = np.linalg.inv(A)
print("A^-1 =\n", inv_A)

# 6. Giải hệ Ax = b
b = np.array([5, 7])
solution = np.linalg.solve(A, b)
print("Nghiệm hệ phương trình:", solution)