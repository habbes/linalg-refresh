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
        # create new plane instead of mutating so that the basepoint
        # can be properly set
        self.planes[row] = Plane(coefficient * p.normal_vector,
            coefficient * p.constant_term)

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        """Adds the multiple of a row to another row in the system"""
        p1 = self.planes[row_to_add]
        p2 = self.planes[row_to_be_added_to]
        self.planes[row_to_be_added_to] = Plane(
            p2.normal_vector + (coefficient * p1.normal_vector),
            p2.constant_term + (coefficient * p1.constant_term)
        )
    
    def compute_triangular_form(self):
        """Returns a version of this system
        in triangular form"""
        s = deepcopy(self)
        leading_idx = s.indices_of_first_nonzero_terms_in_each_row()
        for row in range(len(s.planes)):
            # if leading column at this row has 0 coefficient
            # swap with the first row below that has a non-zero
            # coefficient at the leading column of this row
            if not leading_idx[row] == row:
                try:
                    row_to_swap = leading_idx.index(row, row)
                except ValueError as e:
                    # there's no row where this var is a leading term
                    continue
                s.swap_rows(row, row_to_swap)
                leading_idx[row], leading_idx[row_to_swap] = \
                    leading_idx[row_to_swap], leading_idx[row]
            # eliminate the leading term at this row in the rows
            # below
            for other in range(row + 1, len(s.planes)):
                cur_c = s.planes[row].normal_vector[row]
                other_c = s.planes[other].normal_vector[row]
                if not other_c == 0:
                    m = - (other_c / cur_c)
                    s.add_multiple_times_row_to_row(m, row, other)
                    try:
                        leading_idx[other] = \
                            Plane.first_nonzero_index(s.planes[other].normal_vector)
                    except Exception as e:
                        if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                            leading_idx[other] = -1
        return s

    def compute_rref(self):
        """Returns a version of this system in row-reduced
        echelon form"""
        tf = self.compute_triangular_form()
        # reduce the rows from bottom to top
        for row in range(min(tf.dimension, len(tf.planes)) - 1, -1, -1):
            coef = tf.planes[row].normal_vector[row]
            print("coef", coef)
            # if the leading var has a non-0 coefficient
            # reduce its coefficient to 1
            if MyDecimal(coef).is_near_zero():
                continue
            if not coef == 1:
                tf.multiply_coefficient_and_row(Decimal(1/coef), row)
            # eliminate this var in all rows above
            for other in range(0, row):
                other_coef = tf.planes[other].normal_vector[row]
                if not MyDecimal(other_coef).is_near_zero():
                    tf.add_multiple_times_row_to_row(-other_coef,
                        row, other)       
        return tf

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
