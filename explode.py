#! /usr/bin env python

import numpy as np

__author__ = "jayarajanjn@gmail.com"
def avg(l):
    return 1.0 * sum(l) / len(l)


def explode(value, min_, max_, size):
    solution = (0, list(np.zeros(size)))
    while(abs(value - solution[0]) >= 0.05):
        l = value + 2 * np.random.randn(size)
        l_ = [max((min((int(i), max_)), min_)) for i in l]
        solution = (avg(l_), l_)
        print '.',
    print
    return solution


if __name__ == '__main__':
    print explode(9.5, 0, 10, 12)
