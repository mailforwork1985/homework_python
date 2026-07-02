import math

def square(x):
    S = x*x
    return math.ceil(S)

lenght_side = int(input("Введите длину стороны квадрата:"))

result = square(lenght_side)

print(f"Площадь = {result}")