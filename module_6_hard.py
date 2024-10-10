""" Задание "Они все так похожи":
Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube,
объекты которых будут обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и
 для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры."""


import math


class Figure:  # Базовый класс для фигур
    sides_count = 0  # Количество сторон фигуры (устанавливается в подклассах)

    def __init__(self, color, *sides, filled=False):  # Инициализация цвета, сторон и заполненности фигуры
        self.__sides = sides  # Список сторон фигуры
        self.__color = color  # Цвет фигуры
        self.filled = filled  # Флаг, заполнена ли фигура

    def get_color(self):  # Получение цвета фигуры
        return self.__color

    def __is_valid_color(self, r, g, b):  # Проверка корректности RGB цвета
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):  # Установка нового цвета, если он валиден
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b


    def __is_valid_sides(self, *sides):  # Проверка корректности сторон
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, int) and side <= 0:
                return False
        return True

    def get_sides(self):  # Получение сторон фигуры
        return self.__sides

    def __len__(self):   # Переопределение функции len для получения периметра фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):  # Установка новых сторон, если они валидны
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1  # У круга одна сторона (периметр)

    def __init__(self, __color, __sides,):
        super().__init__(__color, __sides)  # Инициализация базового класса
        self.__radius = __sides / (2 * math.pi)  # Вычисление радиуса круга

    def get_square(self):  # Вычисление площади круга
        area_circle = math.pi * (self.__radius ** 2)
        return area_circle


class Triangle(Figure):
    sides_count = 3  # У треугольника три стороны

    def __init__(self, __color, *__sides, height, filled=False):
        super().__init__(__color, __sides, filled)
        self.__height = height  # Высота треугольника

    def get_square(self):  # Вычисление площади треугольника по формуле Герона
        p = 0.5 * (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2])
        area_triangle = (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5
        return area_triangle

class Cube(Figure):
    sides_count = 12  # У куба 12 сторон (ребер)
    def __init__(self, color, side, filled=False):
        cube_sides = [side] * 12  # Все 12 ребер имеют одинаковую длину
        super().__init__(color, *cube_sides, filled=filled)   # Инициализация базового класса


    def get_volume(self):  # Вычисление объема куба
        return self.get_sides()[0] ** 3  # Объем = длина ребра в кубе


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
