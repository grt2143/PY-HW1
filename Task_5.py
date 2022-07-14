# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 
# 2D пространстве.

#*Пример:*
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

import math

def input_coords(text):

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
        if coord.isdigit():
            coord = int(coord)
            if is_minus:
                coord *= -1
            int_test = False
        else:
            print("Введенное значение не является числом")
    return coord

x1 = input_coords("Введите x-координату 1й точки: ")
y1 = input_coords("Введите y-координату 1й точки: ")
x2 = input_coords("Введите x-координату 2й точки: ")
y2 = input_coords("Введите y-координату 2й точки: ")

dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Расстояние между точками равно -> {dist:.2f}")