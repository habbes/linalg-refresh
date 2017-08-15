"""
vector module

contains Vector class which
encapsulates a basic implementation
of vector operations
"""
import math
from numbers import Number
from decimal import Decimal, getcontext

# 3 decimal places
getcontext().prec = 30

class Vector(object):
    """Represents an n-dimentional vector"""
    def __init__(self, *coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def magnitude(self):
        """Returns the magnitude of the vector"""
        sum_sq = sum([x**2 for x in self.coordinates])
        return sum_sq.sqrt()

    def normalize(self):
        """Computes the normalized version of this vector"""
        return (Decimal(1)/abs(self)) * self

    def scalar_mult(self, const):
        """Performs a scalar multiplication"""
        const = Decimal(const)
        new_coords = [x * const for x in self.coordinates]
        return Vector(*new_coords)

    def dot(self, other):
        """Computes the dot product"""
        return sum([x * y for x, y in zip(self.coordinates, other.coordinates)])

    def multiply(self, other):
        """Performs scalar multiplication or dot
        product depending on the type of other"""
        if isinstance(other, Number):
            return self.scalar_mult(other)
        elif isinstance(other, Vector):
            return self.dot(other)
        raise TypeError

    def angle(self, other, degrees=False):
        """Computes the angle between two vectors
        acos(v dot w/||v||*||w||)"""
        theta = math.acos(self.normalize() * other.normalize())
        if not degrees:
            return theta
        else:
            return math.degrees(theta)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, other):
        new_coords = [x + y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(*new_coords)

    def __sub__(self, other):
        new_coords = [x - y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(*new_coords)

    __abs__ = magnitude
    __mul__ = multiply
    __rmul__ = multiply
