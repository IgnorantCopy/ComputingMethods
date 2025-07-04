import numpy as np


def power(A: np.ndarray, u: np.ndarray, eps: float):
    v = np.max(u)
    while True:
        print(u, v)
        print()
        new_u = A @ u.T
        v_max = np.max(new_u)
        new_u = new_u / v_max
        if abs(v_max - v) < eps:
            v = v_max
            u = new_u
            break
        v = v_max
        u = new_u
    return u, v


if __name__ == '__main__':
    A = np.array([[14/27, 11/27, 5/27],
                  [11/27, -1/27, -2/27],
                  [5/27, 2/27, -4/27]])
    u = np.array([1, 1, 1])
    print(power(A, u, 1e-3))
