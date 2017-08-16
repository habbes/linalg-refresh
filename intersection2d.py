# 2D lines and intersections

from linalg.line import Line, SameLineError, NoIntersectionError
from linalg.vector import Vector

exercises = [
    (
        Line(Vector('4.046', '2.836'), '1.21'),
        Line(Vector('10.115', '7.09'), '3.025')
    ),
    (
        Line(Vector('7.204', '3.182'), '8.68'),
        Line(Vector('8.172', '4.114'), '9.883')
    ),
    (
        Line(Vector('1.182', '5.562'), '6.744'),
        Line(Vector('1.773', '8.343'), '9.525')
    )
]

for i, ls in enumerate(exercises):
    l1, l2 = ls
    num = "{}.".format(i)
    try:
        x = l1.intersection_with(l2)
        print(num, "Intersection:", x)
    except SameLineError:
        print(num, "Same line: infinitely many intersections")
    except NoIntersectionError:
        print(num, "No intersection point: parallel lines")
