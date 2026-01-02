import cython
from libc.math cimport sin

@cython.boundscheck(False)
@cython.wraparound(False)
def integrate_cy(double a, double b, int n_iter=100000):
    """
    Cython-версия интегрирования sin(x) с отпущенным GIL.
    """
    cdef double acc = 0.0
    cdef double step = (b - a) / n_iter
    cdef int i
    cdef double x

    with nogil:
        for i in range(n_iter):
            x = a + i * step
            acc += sin(x) * step
    return acc