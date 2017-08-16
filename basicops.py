from linalg.vector import Vector

# 1. addition
v1 = Vector(8.218, -9.341)
v2 = Vector(-1.129, 2.111)
print(v1, "+", v2, "=", v1 + v2)

# 2. subtraction
v1 = Vector(7.119, 8.215)
v2 = Vector(-8.223, 0.878)
print(v1, "-", v2, "=", v1 - v2)

# 3. scalar multiplication
v = Vector(1.671, -1.012, -0.318)
x = 7.41
print("{}{}".format(x,v), "=", x * v)
