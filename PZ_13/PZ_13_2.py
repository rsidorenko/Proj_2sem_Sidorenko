import numpy as np
import random

# Создаем матрицу 3х3 со случайно заполненными элементами
matrix = [[random.randint(1, 10) for j in range(3)] for i in range(3)]

# Создаем одномерный динамический массив соответствующей размерности
array = [random.randint(1, 10) for i in range(3)]

# Выводим матрицу и массив до замены
print("Матрица до замены:")
for a in matrix:
    print(a)
print("Одномерный массив:")
print(array)

# Заменяем элементы третьей строки матрицы элементами из массива
for j in range(3):
    matrix[2][j] = array[j]

# Выводим матрицу и массив после замены
print("Матрица после замены:")
for row in matrix:
    print(row)