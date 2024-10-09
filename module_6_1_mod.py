class Animal:
    alive = True  # Атрибут класса
    fed = False    # Атрибут класса

    def __init__(self, name):
        self.name = name  # Индивидуальное название каждого животного

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                self.fed = True
                print(f"{self.name} съел {food.name}")
            else:
                self.alive = False
                print(f"{self.name} не стал есть {food.name}")
        else:
            print(f"{self.name} не ест {food.name}")

    def status(self):
        return f"Имя: {self.name}, Жив: {self.alive}, Накормлен: {self.fed}"


class Plant:
    edible = False  # Атрибут класса

    def __init__(self, name):
        self.name = name  # Индивидуальное название каждого растения

    def status(self):
        return f"Имя: {self.name}, Съедобное: {self.edible}"


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        # Цветок по умолчанию не съедобен
        self.edible = False


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        # Фрукт является съедобным
        self.edible = True


# Пример использования классов
if __name__ == "__main__":
    a1 = Animal('Волк с Уолл-Стрит')
    a2 = Animal('Хатико')
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