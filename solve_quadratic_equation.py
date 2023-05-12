import cmath

a = float(input())
b = float(input())
c = float(input())

root_1 = 0
root_2 = 0

discriminant = b**2 - (4*a*c)

if discriminant < 0:
    root_1 = (-b-cmath.sqrt(discriminant))/(2*a)
    root_2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
else:
    root_1 = (-b - (discriminant)**0.5) / (2 * a)
    root_2 = (-b + (discriminant)**0.5) / (2 * a)

print(root_1, root_2)