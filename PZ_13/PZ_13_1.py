import numpy as np
import random

# Создаем матрицу 3х3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Выводим матрицу перед заменой
print("Матрица до замены столбца:")
for row in matrix:
    print(row)

# Заменяем элементы последнего столбца на -1
for row in matrix:
    row[-1] = -1

# Выводим матрицу после замены
print("Матрица после замены столбца:")
for row in matrix:
    print(row)