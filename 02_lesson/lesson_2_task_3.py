import math


def square(side):
    area = side * side
    return math.ceil(area)


side = float(input("Введите длину стороны квадрата: "))
result = square(side)
print(f"Площадь квадрата со стороной {side}: {result}")
