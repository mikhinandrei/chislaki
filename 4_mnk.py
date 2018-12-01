import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 20, 20)

y = [5, 6, 8, 10, 12, 13, 12, 10, 8, 10, 8, 11, 7, 9, 11, 10, 9, 12, 11, 6]

x_sums = [sum(x**i)/20 for i in range(1, 9)]
xy_sums = [sum(y * x**i)/20 for i in range(5)]

print(xy_sums)

A = np.array([
        [1, *x_sums[0:4]],
        x_sums[0:5],
        x_sums[1:6],
        x_sums[2:7],
        x_sums[3:],
    ])

print(A)

B = np.array(xy_sums)

e, d, c, b, a = np.linalg.solve(A, B)

y_new = [a*x_**4 + b*x_**3 + c*x_**2 + d*x_ + e for x_ in x]

fig = plt.figure()
graph1 = plt.plot(x, y)
graph2 = plt.plot(x, y_new)
plt.show()