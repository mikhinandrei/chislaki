import matplotlib.pyplot as plt
import numpy as np


def lagrange(X, Y, i, j):
    summ = 0  # счётчик суммы
    for k in range(0, 6):  #  Цикл Суммирования
        prod = 1
        for m in range(0, 6):  #Цикл произведения
            if k != m:
                prod *= (i - X[j + m]) / (X[j + k] - X[j + m])
        summ += Y[j + k] * prod
    return summ


X = np.linspace(1, 20, 20)

Y = [5, 6, 8, 10, 12, 13, 12, 10, 8, 10, 8, 11,
     7, 9, 11, 10, 9, 12, 11, 6]

i = 1
xlist = np.linspace(1, 20, 77)  # массив для построения графика
ylist = []  # масиив для построения графика
while i < 4:
    ylist.append(lagrange(X, Y, i, 0))
    print(lagrange(X, Y, i, 0))
    i += 0.25

j = 1
while j <= 13:  # цикл для построения интерполированных точек с шагом 0,25 и границами(5;17,75)
    ylist.append(lagrange(X, Y, j + 3, j))
    print(lagrange(X, Y, j + 3, j))
    ylist.append(lagrange(X, Y, j + 3.25, j))
    print(lagrange(X, Y, j + 3.25, j))
    ylist.append(lagrange(X, Y, j + 3.5, j))
    print(lagrange(X, Y, j + 3.5, j))
    ylist.append(lagrange(X, Y, j + 3.75, j))
    print(lagrange(X, Y, j + 3.75, j))
    j += 1

i = 17 # цикл для построения интерполированных точек с шагом 0,25 и границами(18;20)
while i <= 20:
    ylist.append(lagrange(X, Y, i, 14))
    print(lagrange(X, Y, i, 14))
    i += 0.25
i = 1

plt.plot(X, Y, '-s')
plt.plot(xlist, ylist, '-*')
plt.show()