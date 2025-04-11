from math import *

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    result = 0
    x = a
    for i in range(1, n):
        x += h
        result += 2 * f(x)
    result += f(a) + f(b)
    result *= h / 2
    return result


def simpson(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        x = a + (i + 0.5) * h
        result += 4 * f(x)
    for i in range(1, n):
        x = a + i * h
        result += 2 * f(x)
    result += f(a) + f(b)
    result *= h / 6
    return result


def romberg(f, a, b, epsilon):
    k = 1
    h = b - a
    T = [(b - a) / 2 * (f(a) + f(b))]
    print(T[0])
    while True:
        newT = [0 for _ in range(k + 1)]
        newT[0] = trapezoidal(f, a, b, 2 ** k)
        print(newT[0], end=" ")
        for i in range(1, k + 1):
            newT[i] = (4 ** i * newT[i - 1] - T[i - 1]) / (4 ** i - 1)
            print(newT[i], end=" ")
        print()
        if abs(newT[k] - T[k - 1]) < epsilon:
            return newT[k]
        T = newT
        k += 1
        h /= 2


if __name__ == '__main__':
    f = lambda x: 2 / sqrt(pi) * exp(-x)
    print(romberg(f, 0, 1, 1e-5))