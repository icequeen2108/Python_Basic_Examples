sides = [float(input()), float(input()), float(input())]

semi_perimeter = (sides[0] + sides[1] + sides[2])/2

area = (semi_perimeter*(semi_perimeter-sides[0])*(semi_perimeter-sides[1])*(semi_perimeter-sides[2])) ** 0.5
print(area)
print(f"{area:.2f}")
print(f"{area:.0f}")