import math

class Figure:
    sides_count = 0
    def __init__(self, color, *sides, filled = False):
        self.__color = list(color)
        count = 0
        self.__sides = []
        for side in sides:
            count += 1
        if count == self.sides_count:
            for side in sides:
                self.__sides.append(side)
        elif count == 1:
            for i in range(self.sides_count):
                self.__sides.append(list(sides)[0])
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r,g,b):
        valid = True
        if not 0 <= r <= 255:
            valid = False
        if not 0 <= g <= 255:
            valid = False
        if not 0 <= b <= 255:
            valid = False
        return valid

    def set_color(self, r, g, b):
        valid = self.__is_valid_color(r, g, b)
        if valid:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        count = 0
        valid = True
        for arg in args:
            if not isinstance(arg, int) or arg <=0:
                valid = False
            count += 1
        if count != self.sides_count:
            valid = False
        return valid

    def get_sides(self):
        return self.__sides

    def __len__(self):
        p = 0
        for side in self.__sides:
            p += side
        return p

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = []
            for side in new_sides:
                self.__sides.append(side)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.radius = self._Figure__sides[0]/2/math.pi

    def get_square(self):
        return math.pi * self.radius ** 2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        p = self._Figure__len__()/2
        return math.sqrt(p * (p - self._Figure__sides[0]) * (p - self.__sides[1])(p - self.__sides[2]))

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = []
        for i in range(12):
            self.__sides.append(self._Figure__sides[0])

    def get_volume(self):
        return self.__sides[0] ** 3

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

triangle1 = Triangle((250, 15, 56), (3, 4, 5))
print(triangle1.get_color())
triangle1.set_color(89,56,200)
print(triangle1.get_color())
triangle1.set_sides(3,4,2)
print(triangle1.get_sides())
print(len(triangle1))
