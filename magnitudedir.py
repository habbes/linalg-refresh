# Magnitude and direction

from vector import Vector

# Magnitude
v = Vector(-0.221, 7.437)
print("Magnitude of", v, "=", abs(v))
v = Vector(8.813, -1.331, -6.247)
print("Magnitude of", v, "=", abs(v))

# Normalization
v = Vector(5.581, -2.136)
print("Normalize", v, ":", v.normalize())
v = Vector(1.996, 3.108, -4.554)
print("Normalize", v, ":", v.normalize())

