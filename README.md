[![PyPI version](https://badge.fury.io/py/pyqplib.svg)](https://badge.fury.io/py/pyqplib)

# PyQPLIB

The package is designed to read [QPLIB](https://qplib.zib.de/) into Python. Usage:

    >>> import pyqplib
    >>> problem = pyqplib.read_problem("/path/to/file.qplib")
    >>> x0 = problem.x0
    >>> obj = problem.obj_val(x0)
    >>> cons = problem.cons_val(x0)
