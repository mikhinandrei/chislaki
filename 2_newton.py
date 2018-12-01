import numpy as np

eps = 1e-10

f = lambda x, y, z: [
    7.5 * x**2 * y**2 * z**2 - 3*z +2.1*y**2 - 5.1,
    -0.2*y**2 + 0.7*x**2*y+2.2*x*z**2 - 10.8086,
    z**3 + x**3
]

W = lambda x, y, z: [
    [15*x*y**2*z**2, 15*y*x**2*z**2 + 4.2*y, 15*z*x**2*y**2 - 3],
    [1.4*x*y + 2.2*z**2, -0.4*y + 0.7*x**2, 4.4*x*z],
    [3*x**2, 0, 3*z**2]
]

Wx = lambda x, y, z: [
    [7.5 * x**2 * y**2 * z**2 - 3*z +2.1*y**2 - 5.1, 15*y*x**2*z**2 + 4.2*y, 15*z*x**2*y**2 - 3],
    [-0.2*y**2 + 0.7*x**2*y+2.2*x*z**2 - 10.8086, -0.4*y + 0.7*x**2, 4.4*x*z],
    [z**3 + x**3, 0, 3*z**2]
]

Wy = lambda x, y, z: [
    [15*x*y**2*z**2, 7.5 * x**2 * y**2 * z**2 - 3*z +2.1*y**2 - 5.1, 15*z*x**2*y**2 - 3],
    [1.4*x*y + 2.2*z**2, -0.2*y**2 + 0.7*x**2*y+2.2*x*z**2 - 10.8086, 4.4*x*z],
    [3*x**2, z**3 + x**3, 3*z**2]
]

Wz = lambda x, y, z: [
    [15*x*y**2*z**2, 15*y*x**2*z**2 + 4.2*y, 7.5 * x**2 * y**2 * z**2 - 3*z +2.1*y**2 - 5.1],
    [1.4*x*y + 2.2*z**2, -0.4*y + 0.7*x**2, -0.2*y**2 + 0.7*x**2*y+2.2*x*z**2 - 10.8086],
    [3*x**2, 0, z**3 + x**3]
]

solution = np.array([0, 0, 0], dtype=np.float64)
solution_k = np.array([int(x) for x in input().split()], dtype=np.float64)

while np.linalg.norm(solution_k - solution) > eps:
    x_n = solution_k[0] - np.linalg.det(Wx(*solution_k))/np.linalg.det(W(*solution_k))
    y_n = solution_k[1] - np.linalg.det(Wy(*solution_k)) / np.linalg.det(W(*solution_k))
    z_n = solution_k[2] - np.linalg.det(Wz(*solution_k)) / np.linalg.det(W(*solution_k))

    solution = np.copy(solution_k)
    solution_k = np.array([x_n, y_n, z_n], dtype=np.float64)

print("x= {}\ny= {}\nz = {}\n".format(*solution), "Проверка: {}".format(f(*solution)))
