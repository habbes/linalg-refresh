# Projection

from linalg.vector import Vector

v = Vector('3.039', '1.879')
b = Vector('0.825', '2.036')
print("1. Projection of v on b:", v.project_on(b))

v = Vector('-9.88', '-3.264', '-8.159')
b = Vector('-2.155', '-9.353', '-9.473')
print("2. Component of v orthognal to b:", 
    v.component_orthogonal_to(b))

v = Vector('3.009', '-6.172', '3.692', '-2.51')
b = Vector('6.404', '-9.144', '2.759', '8.718')
print("3a. Projection of v on b", v.project_on(b))
print("3b. Component of v orthogonal to b:",
    v.component_orthogonal_to(b))

assert(v == v.project_on(b) + v.component_orthogonal_to(b))