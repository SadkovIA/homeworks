class House:
    def __init__(self, name, numbers_of_floor):
        self.name = name
        self.numbers_of_floor = numbers_of_floor

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.numbers_of_floor:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)   # Выводит этажи от 1 до 5
h2.go_to(10)  # Выводит "Такого этажа не существует"