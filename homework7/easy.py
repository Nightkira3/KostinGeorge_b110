__author__ = 'Костин Георгий'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
# TODO:

import math


class Triangle:
    def __init__(self, a, b, c):
        def side_len(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        self.a = a
        self.b = b
        self.c = c
        self.ab = side_len(self.a, self.b)
        self.bc = side_len(self.b, self.c)
        self.ca = side_len(self.c, self.a)

    def calc_area(self):
        semi_perimeter = self.calc_perimeter() / 2

        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.ab)
                         * (semi_perimeter - self.bc)
                         * (semi_perimeter - self.ca))

    def calc_perimeter(self):
        return self.ab + self.bc + self.ca

    def calc_height(self):
        return self.calc_area() / (self.ab / 2)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
# TODO:

class Trapeze:
    def __init__(self, a, b, c, d):
        def side_len(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        def calc_area(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2

            return math.sqrt(semi_perimeter
                             * (semi_perimeter - len1)
                             * (semi_perimeter - len2)
                             * (semi_perimeter - len3))

        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.ab = side_len(self.a, self.b)
        self.bc = side_len(self.b, self.c)
        self.cd = side_len(self.c, self.d)
        self.da = side_len(self.d, self.a)

        self.diagonal_ac = side_len(self.c, self.a)
        self.diagonal_bd = side_len(self.b, self.d)
        self.perimeter = self.ab + self.bc + self.cd + self.da

        self.area = calc_area(self.ab, self.diagonal_bd, self.da) \
                    + calc_area(self.diagonal_bd, self.bc, self.cd)

    def calc_perimeter(self):
        if self.diagonal_ac == self.diagonal_bd:
            return True
        return False
