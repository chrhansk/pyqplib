import scipy.sparse


def sparse_zero(shape):
    assert shape.ndim == 2
    return scipy.sparse.coo_matrix(([], ([], [])), shape)
