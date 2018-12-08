x = int(input())

f = lambda x: 9.2*x**5 - 3.25*x**3 + 21.3*x**2 - 43.7
der_f = lambda x: 46*x**4 + 9.75*x**2 + 42.6*x

x_n = x - f(x)/der_f(x)

while abs(x_n - x) > 1e-10:
    x = x_n
    x_n = x - f(x) / der_f(x)

print(x_n)
