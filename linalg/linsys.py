"""
Linear System module
"""
from decimal import Decimal, getcontext
from copy import deepcopy

from .vector import Vector
from .plane import Plane
from .mydecimal import MyDecimal

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def swap_rows(self, row1, row2):
        """Swaps two rows in the system"""
        self.planes[row1], self.planes[row2] = self.planes[row2], self.planes[row1]

    def multiply_coefficient_and_row(self, coefficient, row):
        """Multiplies the row at the specified index by the coeffiecient"""
        p = self.planes[row]
        p.normal_vector = coefficient * p.normal_vector
        p.constant_term = coefficient * p.constant_term

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        """Adds the multiple of a row to another row in the system"""
        source = deepcopy(self.planes[row_to_add])
        target = self.planes[row_to_be_added_to]
        source.normal_vector = coefficient * source.normal_vector
        source.constant_term = coefficient * source.constant_term
        target.normal_vector = target.normal_vector + source.normal_vector
        target.constant_term = target.constant_term + source.constant_term

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret
