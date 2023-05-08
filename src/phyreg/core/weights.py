from numpy import array, max


def weight_routine(points, weights):
    if not weights:
        weights = [1 for _ in range(len(points))]
    elif isinstance(weights, list):
        if len(points) != len(weights):
            raise TypeError("Length of points and weights does not match.")
    return weights


def reversed_err(p, ex_f):
    """Weight is the difference of the maximal error and the specific error.
    Problem: Least precise value gets weight 0."""
    err = array([abs(ex_f(ele[0]) - ele[1]) for ele in p])
    return max(err) - err
