"""
line module
"""
from .mydecimal import MyDecimal as Decimal
from .vector import Vector


class Line(object):
    """Represents a line"""
    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'
    PARALLEL_OR_COINCIDENT = 'The lines are parallel or coincident'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        """Computes and sets the basepoint vector of
        the line"""
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension
            # find nonzero coefficient
            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]
            # basepoint has 0's expect for the selected
            # coefficient index
            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(*basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def is_parallel_to(self, other):
        """Check whether two lines are parallel"""
        return self.normal_vector.is_parallel_to(other.normal_vector)

    def is_equal_to(self, other):
        """Checks whether the two lines coincident
        i.e. consist of the same set of points"""
        # coincident lines must be parallel
        if not self.is_parallel_to(other):
            return False
        # find point on this line
        p1 = self.basepoint
        # find point on other line
        p2 = other.basepoint
        # find vector between p1 and p2
        v = p1 - p2
        # vector between the lines must be
        # orthogonal to each line's normal vector
        # it suffices to check if it's orthogonal
        # to one of them
        return v.is_orthogonal_to(self.normal_vector)

    __eq__ = is_equal_to

    def intersection_with(self, other):
        """Returns the point vector of intersection
        between two lines if the lines have 1 intersection.
        Assumes 2D"""
        if self == other:
            raise SameLineError
        if self.is_parallel_to(other):
            raise NoIntersectionError
        a, b = self.normal_vector.coordinates
        k1 = self.constant_term
        c, d = other.normal_vector.coordinates
        k2 = other.constant_term
        x = (d * k1 - b * k2)/(a*d - b*c)
        y = (-c * k1 + a * k2)/(a*d - b*c)
        return Vector(x, y)

    @staticmethod
    def first_nonzero_index(iterable):
        """Finds the index of the first nonzero
        element in the sequence"""
        for k, item in enumerate(iterable):
            if not Decimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)

class SameLineError(Exception):
    pass

class NoIntersectionError(Exception):
    pass