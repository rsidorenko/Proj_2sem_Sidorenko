# На числовой оси расположены три точки: A, B, C. Определить, какая из двух
# последних точек (B или C) расположена ближе к A, и вывести эту точку и ее
# расстояние от точки A.
import math

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

prov1 = math.sqrt((A - B) ** 2)
prov2 = math.sqrt((A - C) ** 2)

if prov1 < prov2:
    print('Точка B ближе к точке A, расстояние, оно равно: ', prov1)
elif prov1 == prov2:
    print('Точки B и C находятся на одинаковлм расстоянии к точке A: ', prov1)
else:
    print('Точка C ближе к точке A, расстояние, оно равно: ', prov2)