import numpy as np


def cal_B0(A: np.ndarray, b: np.ndarray):
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    B0 = np.linalg.inv(D) @ (L + U)
    f = np.linalg.inv(D) @ b.T
    return B0, f


def cal_G(A: np.ndarray, b: np.ndarray):
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    G = np.linalg.inv(D - L) @ U
    f = np.linalg.inv(D - L) @ b.T
    return G, f


def jacobi(x: np.ndarray, A: np.ndarray, b: np.ndarray, eps=1e-4) -> np.ndarray:
    B0, f = cal_B0(A, b)
    new_x = B0 @ x.T + f
    while max(abs(new_x - x)) > eps:
        x = new_x
        new_x = B0 @ x.T + f
    return new_x


def gauss_seidel(x: np.ndarray, A: np.ndarray, b: np.ndarray, eps=1e-4) -> np.ndarray:
    G, f = cal_G(A, b)
    new_x = G @ x.T + f
    while max(abs(new_x - x)) > eps:
        x = new_x
        new_x = G @ x.T + f
    return new_x


if __name__ == '__main__':
    A = np.array([[1, 0, -0.25, -0.25], [0, 1, -0.25, -0.25], [-0.25, -0.25, 1, 0], [-0.25, -0.25, 0, 1]])
    b = np.array([0.5, 0.5, 0.5, 0.5])
    B0, _ = cal_B0(A, b)
    G, _ = cal_G(A, b)
    print(B0)
    print(G)
    print(np.linalg.eigvals(B0))
    print(np.linalg.eigvals(G))