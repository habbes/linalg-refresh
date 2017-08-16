# Dot product and angle between vectors
import math
from linalg.vector import Vector

# Dot product
v1 = Vector(7.887, 4.138)
v2 = Vector(-8.802, 6.776)
print(v1, "dot", v2, "=", v1 * v2)
v1 = Vector(-5.955, -4.904, -1.874)
v2 = Vector(-4.496, -8.755, 7.103)
print(v1, "dot", v2, "=", v1 * v2)

# Angles
v1 = Vector(3.183, -7.627)
v2 = Vector(-2.668, 5.319)
print("Angle between", v1, "and", v2, "=", v1.angle(v2), "rad")
v1 = Vector(7.35, 0.221, 5.188)
v2 = Vector(2.751, 8.259, 3.985)
print("Angle between", v1, "and", v2, "=", v1.angle(v2, degrees=True), "deg")
