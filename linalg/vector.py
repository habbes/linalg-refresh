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
            # check if 0 vector
            self.is_zero = True
            for c in self.coordinates:
                if not c == Decimal(0):
                    self.is_zero = False
                    break

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

    def is_orthogonal_to(self, other):
        """Checks whether two vectors are orthogonal"""
        if self.is_zero or other.is_zero:
            return True
        return self * other == Decimal(0)

    def is_parallel_to(self, other):
        """Checks whether two vectors are parallel"""
        # return True for 0 vector
        if self.is_zero or other.is_zero:
            return True
        # check if common factor exist between
        # all coordinate pairs, more efficient
        # than checking angle or normalized magnitudes
        factor = None
        for x, y in zip(self.coordinates, other.coordinates):
            # special case for 0, to avoid division errors
            if x == 0 and y == 0:
                continue
            if x == 0 or y == 0:
                return False
            if factor is None: # first non-zero elements
                factor = y / x
                continue
            # subsequent elements
            if not y / x == factor:
                return False
        return True

    def project_on(self, basis):
        """Computes the projection of this vector
        on the specified basis vector"""
        u_basis = basis.normalize()
        return (self * u_basis) * u_basis

    component_parallel_to = project_on

    def component_orthogonal_to(self, basis):
        """Computes the vector component of self that
        is orthogonal to the specified basis vector"""
        return self - self.project_on(basis)

    def cross(self, other):
        """Computes the cross product"""
        if self.dimension > 3 or other.dimension > 3:
            raise Exception("Cross product not supported beyond 3D")
        # add 0 z-index in case of 2D vectors
        v = self if self.dimension == 3 else Vector(*(self.coordinates + ('0',)))
        w = other if other.dimension == 3 else Vector(*(other.coordinates + ('0',)))
        return Vector(
            (v[1] * w[2]) - (v[2] * w[1]),
            -((v[0] * w[2]) - (v[2] * w[0])),
            (v[0] * w[1]) - (v[1] * w[0])
        )

    def parallelogram_area_with(self, other):
        """Computes the area of the parallegogram spanned
        by two vectors"""
        return self.cross(other).magnitude()

    def triangle_area_with(self, other):
        """Computes the area of the triangle
        spanned by two vectors"""
        return self.parallelogram_area_with(other) / 2

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __getitem__(self, key):
        return self.coordinates[key]

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
