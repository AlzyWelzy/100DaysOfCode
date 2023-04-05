# def double(x):
#     return x * 2


double = lambda x: x * 2

print(double(5))


cube = lambda x: x**3
avg = lambda x, y, z: (x + y + z) / 3
avg_cube = lambda x, y, z: (x**3 + y**3 + z**3) / 3
random_formula = (
    lambda x, y, z: (x**3 + y**3 + z**3) / 3 + 2 * (x + y + z) / 3**x**y**z
)


print(cube(5))
print(avg(1, 2, 3))
print(avg_cube(1, 2, 3))
print(random_formula(1, 2, 3))
print(random_formula(1, 2, 3) == avg_cube(1, 2, 3))

print(random_formula(cube(1), avg(1, 2, 3), avg_cube(1, 2, 3)))
