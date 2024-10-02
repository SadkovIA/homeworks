class House:
    houses_history = []  # Атрибут класса для хранения истории домов

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __new__(cls, *args):
        # Создание нового экземпляра
        instance = super(House, cls).__new__(cls)
        house_name = args[0]  # Название дома берём из первого аргумента
        cls.houses_history.append(house_name)  # Добавляем название в историю
        return instance

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # ЖК Акация снесён, но он останется в истории
del h3  # ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

del h1  # ЖК Эльбрус снесён, но он останется в истории