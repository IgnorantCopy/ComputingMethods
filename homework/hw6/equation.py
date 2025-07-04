from math import *


def secant(f, x0, x1, tol=1e-6):
    print("Secant method:", end=' ')
    print(x0, x1, end=' ')
    while abs(x1 - x0) > tol:
        prime = (f(x1) - f(x0)) / (x1 - x0)
        x2 = x1 - f(x1) / prime
        print(x2, end=' ')
        x0, x1 = x1, x2
    return x1


def parabola(f, x0, x1, x2, tol=1e-6):
    print("Parabola method:", end=' ')
    print(x0, x1, x2, end=' ')
    while abs(x2 - x1) > tol:
        a = (f(x1) - f(x0)) / (x1 - x0)
        b = (f(x2) - f(x1)) / (x2 - x1)
        c = (b - a) / (x2 - x0)
        omega = b + c * (x2 - x1)
        term = sqrt(omega ** 2 - 4 * f(x2) * c) * (1 if omega > 0 else -1)
        x3 = x2 - (2 * f(x2)) / (omega + term)
        print(x3, end=' ')
        x0, x1, x2 = x1, x2, x3
    return x2


def binary_search(f, a, b, tol=1e-6):
    print("Binary search method:", end=' ')
    while abs(b - a) > tol:
        print(f"({a}, {b})", end=' ')
        m = (a + b) / 2
        if f(m) == 0:
            return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2


def newton(f, df, x0, tol=1e-6):
    print("Newton's method:", end=' ')
    while abs(f(x0)) > tol:
        print(x0, end=' ')
        x0 -= f(x0) / df(x0)
    return x0


if __name__ == '__main__':
    f = lambda x: x ** 3 - 3 * x - 1
    x0, x1 = 2, 1.9
    print(secant(f, x0, x1, tol=1e-3))
    x0, x1, x2 = 1, 3, 2
    print(parabola(f, x0, x1, x2, tol=1e-3))

    g = lambda x: x - atan(x) - pi
    a = pi / 2 + 1e-6
    b = 3 * pi / 2 - 1e-6
    print(binary_search(g, a, b))
    dg = lambda x: 1 - 1 / (1 + x ** 2)
    x0 = pi
    print(newton(g, dg, x0))