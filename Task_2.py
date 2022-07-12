# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            exp1 = not(x and y and z)
            exp2 = - x or - y or - z
            print(f"{x}/{y}/{z} {exp1 == exp2}")