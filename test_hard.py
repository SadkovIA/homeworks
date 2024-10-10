import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        self.__sides = list(sides)
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, (int, float)) and side > 0 for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, diameter):
        super().__init__(color, diameter)
        self.__radius = diameter / 2

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, height, filled=False):
        super().__init__(color, *sides, filled=filled)
        self.__height = height

    def get_square(self):
        p = sum(self.get_sides()) / 2
        return (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side, filled=False):
        super().__init__(color, *([side] * 12), filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3

# Примеры использования
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)
print(circle1.get_color())  # Изменится

cube1.set_color(300, 70, 15)
print(cube1.get_color())  # Не изменится

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга)
print(len(circle1))

# Проверка объёма (куба)
print(cube1.get_volume())