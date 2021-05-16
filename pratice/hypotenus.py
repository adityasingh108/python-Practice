import math


def hypotenius(perpendicular, base):
    perp_square = perpendicular**2
    base_square = base**2
    hyp_square = perp_square+base_square
    result = math.sqrt(hyp_square)
    return float(result)


perpendicular = int(input("enter the perpendicular of Tringle:"))
base = int(input("enter the base of the tringle "))

print(hypotenius(perpendicular, base))
