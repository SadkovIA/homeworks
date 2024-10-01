class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def __len__(self):
        return self.number_of_floors  # Возвращает количество этажей


    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

# Пример использования класса
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# str
print(h1)  # Выводит: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Выводит: Название: ЖК Акация, кол-во этажей: 20

# len
print(len(h1))  # Выводит: 10
print(len(h2))  # Выводит: 20