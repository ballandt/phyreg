from numpy import array, max, mean


def reversed_err(p, ex_f):
    """Weight is the difference of the maximal error and the specific error."""
    err = array([abs(ex_f(ele[0]) - ele[1]) for ele in p])
    return max(err) - err
