from .core import proportional, weights as weights_mod


__author__ = "Camillo Ballandt"
__date__ = "2023/08/05"
__version__ = "0.1"


def dir_prop(points: list, weights=[]) -> float:
    """Direct proportional regression.
    y = a * x
    Returns parameter 'a'."""
    weights = weights_mod.weight_routine(points, weights)
    return proportional.direct(points, weights)


def ind_prop(points: list, weights=[]) -> float:
    """Indirect proportional regression.
    y = a * x^-1
    Returns parameter 'a'."""
    for ele in points:
        if ele[0] == 0:
            raise ValueError("Must not contain points with x = 0")
    weights = weights_mod.weight_routine(points, weights)
    return proportional.indirect(points, weights)


def sqrt_prop(points: list, weights=[]) -> float:
    """Proportional to square root regression.
    y = a * sqrt(x)
    Returns parameter 'a'."""
    for ele in points:
        if ele[0] < 0:
            raise ValueError("Must not contain points with x < 0")
    weights = weights_mod.weight_routine(points, weights)
    return proportional.square_root(points, weights)


def free_fall(points: list, weights=[], *b) -> list:
    weights = weights_mod.weight_routine(points, weights)
