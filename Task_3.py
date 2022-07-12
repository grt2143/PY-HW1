#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#*Пример:*
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

int_test = True
is_minus = False

while int_test:
    x = input("Введите x-координату: ")
    if x[0] == "-":
        is_minus = True
        x = x.replace("-","")
    if x.isdigit():
        x = int(x)
        if is_minus:
            x = x * -1
        if x != 0:
            int_test = False
        else :
            print("Введите ненулевое значение!")
    else :
        print("Введите числовое значение!")

int_test = True
is_minus = False

while int_test:
    y = input("Введите y-координату: ")
    if y[0] == "-":
        is_minus = True
        y = y.replace("-","")
    if y.isdigit():
        y = int(y)
        if is_minus:
            y = y * -1
        if y != 0:
            int_test = False
        else :
            print("Введите ненулевое значение!")
    else :
        print("Введите числовое значение!")

if x > 0 and y > 0:
    print("-> 1 четверть")
elif x < 0 and y > 0:
    print("-> 2 четверть")
elif x < 0 and y < 0:
    print("-> 3 четверть")
elif x > 0 and y < 0:
    print("-> 4 четверть")