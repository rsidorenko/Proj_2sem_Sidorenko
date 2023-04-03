# Создаем два текстовых файла с последовательностями целых чисел
with open("file1.txt", "w") as f1:
    f1.write("1 -2 3 -4 5")
with open("file2.txt", "w") as f2:
    f2.write("-6 7 8 -9 10")

# Открываем первые два файла для чтения
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    # Читаем данные и преобразуем их в списки чисел
    seq1 = [int(x) for x in f1.read().split()]
    seq2 = [int(x) for x in f2.read().split()]

# Создаем новый текстовый файл для записи результатов
with open("results.txt", "w") as f:
    # Выводим элементы первого и второго файлов
    f.write("Элементы первого файла: ")
    for x in seq1:
        f.write(str(x) + " ")
    f.write("\n")

    f.write("Элементы второго файла: ")
    for x in seq2:
        f.write(str(x) + " ")
    f.write("\n")

    # Выводим количество элементов первого и второго файлов
    f.write("Количество элементов первого файла: " + str(len(seq1)) + "\n")
    f.write("Количество элементов второго файла: " + str(len(seq2)) + "\n")

    # Выводим количество элементов, общих для двух файлов
    common_elements = set(seq1).intersection(set(seq2))
    f.write("Количество общих элементов: " + str(len(common_elements)) + "\n")

    # Выводим количество четных элементов первого файла
    even_count = sum(1 for x in seq1 if x % 2 == 0)
    f.write("Количество четных элементов первого файла: " + str(even_count) + "\n")

    # Выводим количество нечетных элементов второго файла
    odd_count = sum(1 for x in seq2 if x % 2 != 0)
    f.write("Количество нечетных элементов второго файла: " + str(odd_count) + "\n")

print("Результаты записаны в файл 'results.txt'")
with open("results.txt", "r") as f:
    contents = f.read()
    print("Содержимое файла:\n" + contents)