import scipy.sparse


def sparse_zero(shape):
    assert len(shape) == 2
    return scipy.sparse.coo_matrix(([], ([], [])), shape)
