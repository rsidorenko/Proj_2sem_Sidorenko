# Вывод содержимого файла
with open("text18-29.txt", "r") as file:
    print(file.read())

# Подсчет количества символов
with open("text18-29.txt", "r") as file:
    text = file.read()
    print("Количество символов в тексте:", len(text))

# Создание и запись в новый файл
with open("text_poem.txt", "w") as file:
    lines = text.split("\n")
    file.write(lines[0] + "\n")
    file.write(lines[1] + "\n")
    file.write(lines[5] + "\n")
    file.write(lines[2] + "\n")
    file.write(lines[3] + "\n")
    file.write(lines[4] + "\n")
    file.write(lines[6] + "\n")

# Вывод содержимого нового файла
with open("text_poem.txt", "r") as file:
    print(file.read())