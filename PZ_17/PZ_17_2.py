class Animal:
    def __init__(self, species, legs, fur_color):
        self.species = species
        self.legs = legs
        self.fur_color = fur_color

class Dog(Animal):
    def __init__(self, species, legs, fur_color, name, breed):
        super().__init__(species, legs, fur_color)
        self.name = name
        self.breed = breed

# Создание экземпляра класса "Собака"
my_dog = Dog("Swag", 4, "черный", "Рекс", "Немецкая овчарка")

# Вывод атрибутов класса "Животное"
print("Это", my_dog.species, "с", my_dog.legs, "лапами и шерстью", my_dog.fur_color)

# Вывод атрибутов класса "Собака"
print("Его кличка -", my_dog.name, "и он породы", my_dog.breed)