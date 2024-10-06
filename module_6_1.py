class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        raise NotImplementedError("Этот метод должен быть переопределен в наследниках.")

    def status(self):
        return f"Имя: {self.name}, Жив: {self.alive}, Накормлен: {self.fed}"


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

    def status(self):
        return f"Имя: {self.name}, Съедобное: {self.edible}"


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False  # По умолчанию цветок не съедобен


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукт съедобен


# Пример использования классов
if __name__ == "__main__":
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)  # Волк с Уолл-Стрит
    print(p1.name)  # Цветик семицветик

    print(a1.alive)  # True
    print(a2.fed)  # False

    a1.eat(p1)  # Волк с Уолл-Стрит не стал есть Цветик семицветик
    a2.eat(p2)  # Хатико съел Заводной апельсин

    print(a1.alive)  # False
    print(a2.fed)  # True