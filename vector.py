from numbers import Number

class Vector(object):
    def __init__(self, coordinates):
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
        combined = self._combine_coords(other)
        return tuple(map(lambda x: x[0]+x[1], combined))

    def __sub__(self, other):
        combined = self._combine_coords(other)
        return tuple(map(lambda x: x[0]-x[1]), combined)

    def __mul__(self, other):
        if not isinstance(other, Number):
            raise TypeError("Scalar multiplication requires a number")
        return tuple(map(lambda x: x * other))

    def _combine_coords(self, other):
        return zip(self.coordinates, other.coordinates)
  