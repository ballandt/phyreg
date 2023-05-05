"""Forms of proportionality"""
from math import sqrt


def direct(p, w):
    return sum([w[i]*ele[0]*ele[1] for i, ele in enumerate(p)]) / sum([w[i]*ele[0]**2 for i, ele in enumerate(p)])


def indirect(p, w):
    return sum([w[i]*ele[1] / ele[0] for i, ele in enumerate(p)]) / sum([w[i]*1 / ele[0] ** 2 for i, ele in enumerate(p)])


def square_root(p, w):
    return sum([w[i]*ele[1] * sqrt(ele[0]) for i, ele in enumerate(p)]) / sum([w[i]*ele[0] for i, ele in enumerate(p)])
