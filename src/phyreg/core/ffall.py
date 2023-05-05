"""Free fall"""
from numpy.linalg import solve


def fixed_b(p, w, b):
    return (sum([w[i]*ele[0]**2*ele[1] for i, ele in enumerate(p)]) - b*sum([w[i]*ele[0]**2 for i, ele in enumerate(p)])) / sum([w[i]*ele[0]**4 for i, ele in enumerate(p)])


def general(p, w):
    b = [
        sum([w[i]*ele[0] ** 2 * ele[1] for i, ele in enumerate(p)]),
        sum([w[i]*ele[1] for i, ele in enumerate(p)])
    ]
    A = [
        [sum([w[i]*ele[0] ** 4 for i, ele in enumerate(p)]), sum([w[i]*ele[0] ** 2 for i, ele in enumerate(p)])],
        [sum([w[i]*ele[0] ** 2 for i, ele in enumerate(p)]), sum(w)]
    ]
    return list(solve(A, b))
