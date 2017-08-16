# Planes

from linalg.plane import Plane
from linalg.vector import Vector

excerices = [
    (
        Plane(Vector('-0.412', '3.806', '0.728'), '-3.46'),
        Plane(Vector('1.03', '-9.515', '-1.82'), '8.65')
    ),
    (
        Plane(Vector('2.611', '5.528', '0.283'), '4.6'),
        Plane(Vector('7.715', '8.306', '5.342'), '3.76')
    ),
    (
        Plane(Vector('-7.926', '8.625', '-7.212'), '-7.952'),
        Plane(Vector('-2.642', '2.875', '-2.404'), '-2.443')
    )
]

for i, ps in enumerate(excerices):
    num = "{}.".format(i + 1)
    p1, p2 = ps
    if p1 == p2:
        print(num, "The planes are equal")
    elif p1.is_parallel_to(p2):
        print(num, "The planes are parallel but not equal")
    else:
        print(num, "The planes are not parallel")
