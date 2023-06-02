# Составить функцию, которая напечатает сорок любых символов.
def random_chars():
    import random
    for i in range(40):
        char = chr(random.randint(33, 126))
        print(char, end="")
    print()

random_chars()