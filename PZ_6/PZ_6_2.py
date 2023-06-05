# Дан целочисленный список A размера N. Переписать в новый целочисленный
# список B того же размера вначале все элементы исходного списка с четными
# номерами, а затем — с нечетными: A2, А4, А6, …, A1, A3, А5, … . Условный
# оператор не использовать.
import random
A = []
N = input("Введите размер списка: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Введите целое число!')
        N = input("Введите размер списка: ")
F = N
while F > 0:
    F -= 1
    A.append(random.randint(-100, 100))
print("Первоначальный список", A)
B = A[1::2] + A[::2]
print("Конечный список", B)