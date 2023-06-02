#Даны положительные числа A, B, C. На прямоугольнике размера A х B размещено
#максимально возможное количество квадратов со стороной C (без наложений).
#Найти количество квадратов, размещенных на прямоугольнике. Операции
#умножения и деления не использовать.

A = input('Введите точку A:')
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print('Введите целое число!')
        A = input('Введите точку A:')
B = input('Введите точку B:')
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print('Введите целое число!')
        B = input('Введите точку B:')
C = input('Введите точку C:')
while type(C) != int:
    try:
        C = int(C)
    except ValueError:
        print('Введите целое число!')
        C = input('Введите точку C:')
count1 = 0
count2 = 0
while A >= C:
    A -= C
    count1 += 1
while B >= C:
    B -= C
    count2 +=  count1

print('Кол-во квадратов:', count2)