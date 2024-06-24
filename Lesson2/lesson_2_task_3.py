import math



def square(side):
	if isinstance (side, int):
		return side ** 2
	else:
		return math.ceil (side ** 2)
	
side = float(input("Какова длинна сторон?"))
area = square(side)
print(f"Площадь квадрата со стороной {side} равна {area}")
