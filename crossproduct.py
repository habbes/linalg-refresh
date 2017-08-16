# Cross product

from linalg.vector import Vector

v = Vector('8.462', '7.893', '-8.187')
w = Vector('6.984', '-5.975', '4.778')
cross = v.cross(w)
print("1. Cross product of v and w:", cross)

# cross product of v and w must be orthogonal to
# both v and w
assert(v * cross == 0)
assert(w * cross == 0)

v = Vector('-8.987', '-9.838', '5.031')
w = Vector('-4.268', '-1.861', '-8.866')
print("2. Area of parallegram spanned by v and w:", v.parallelogram_area_with(w))

v = Vector('1.5', '9.547', '3.691')
w = Vector('-6.007', '0.124', '5.772')
print("3. Area of triangle spanned by v and w:", v.triangle_area_with(w))
