"""Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vegetables')"""


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        # Метод для получения всех продуктов из файла
        try:
            with open(self.__file_name, 'r') as file:
                products = file.read().strip()  # Считываем все строки в одну строку
                return products  # Возвращаем все продукты как единую строку
        except FileNotFoundError:
            return ''  # Если файл не найден, возвращаем пустую строку

    def add(self, *products):
        # Получаем существующие продукты как множество для быстрого поиска
        existing_products = self.get_products().splitlines()
        existing_products_set = {line.split(', ')[0] for line in existing_products}

        for product in products:
            if product.name in existing_products_set:
                # Если продукт с таким именем уже есть, выводим сообщение
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                # Добавляем продукт в файл
                with open(self.__file_name, 'a') as file:
                    file.write(f'{product}\n')  # Записываем новый продукт в файл


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())