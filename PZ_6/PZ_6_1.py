# Дан список A размера N и целое число K (1 < K < N). Преобразовать список,
# увеличив каждый его элемент на исходное значение элемента AK
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
K = 3
print("Первоначальный список", A)
for i in range(len(A)):
    A[i] += A[K-1]
print("Конечный список", A)