from numbers import Number

class Vector(object):
    def __init__(self, *coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, other):
        new_coords = [x + y for x,y in zip(self.coordinates, other.coordinates)]
        return Vector(*new_coords)

    def __sub__(self, other):
        new_coords = [x - y for x,y in zip(self.coordinates, other.coordinates)]
        return Vector(*new_coords)

    def __rmul__(self, other):
        if not isinstance(other, Number):
            raise TypeError("Scalar multiplication requires a number")
        new_coords = [x * other for x in self.coordinates]
        return Vector(*new_coords)
