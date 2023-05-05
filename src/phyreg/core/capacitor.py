import numpy as np


def f(xi, p):
    return np.array([ele[1] - xi[0] * np.e ** (xi[1] * ele[0]) - xi[2] for ele in p])


def Df(xi, p):
    return np.array([[-np.e**(xi[1] * ele[0]), -xi[0] * ele[0] * np.e ** (xi[1] * ele[0]), -1] for ele in p])


def charge(p, x, s):
    for i in range(s):
        Dfi = Df(x, p)
        fi = f(x, p)
        delta = np.linalg.solve(Dfi.T @ Dfi, -Dfi.T @ fi)
        t = 1
        while np.linalg.norm(f(x + t*delta, p))**2 > np.linalg.norm(f(x, p))**2:
            t /= 2
        x = x + t*delta
    return x
