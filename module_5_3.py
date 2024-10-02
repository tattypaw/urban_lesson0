class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        result = "Название: " + self.name + ", количество этажей: " + str(self.number_of_floors)
        return result

    def __eq__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors == other.number_of_floors
        else:
            print("Объект другого класса. Сравнение невозможно!")
            return

    def __lt__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors < other.number_of_floors
        else:
            print("Объект другого класса. Сравнение невозможно!")
            return

    def __le__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors <= other.number_of_floors
        else:
            print("Объект другого класса. Сравнение невозможно!")
            return

    def __gt__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors > other.number_of_floors
        else:
            print("Объект другого класса. Сравнение невозможно!")
            return

    def __ge__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors >= other.number_of_floors
        else:
            print("Объект другого класса. Сравнение невозможно!")
            return

    def __ne__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors != other.number_of_floors
        else:
            print("Объект другого класса. Сравнение невозможно!")
            return

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)
        elif isinstance(other, House):
            return House(self.name, self.number_of_floors + other.number_of_floors)
        else:
            print("Объекты должны быть класса House и int или оба объекта должны быть класса House.")
            return

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if not isinstance(other, int):
            print("Правый операнд должен быть типом int или объектом House")
            return
        else:
            self.number_of_floors += other
            return self

    def __sub__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors - other)
        elif isinstance(other, House):
            return House(self.name, self.number_of_floors - other.number_of_floors)
        else:
            print("Объекты должны быть класса House и int или оба объекта должны быть класса House.")
            return

    def __rsub__(self, other):
        if isinstance(other, int):
            return House(self.name, - self.number_of_floors + other)
        elif isinstance(other, House):
            return House(self.name,  - self.number_of_floors + other.number_of_floors)
        else:
            print("Объекты должны быть класса House и int или оба объекта должны быть класса House.")
            return

    def __isub__(self, other):
        if not isinstance(other, int):
            print("Правый операнд должен быть типом int или объектом House")
            return
        else:
            self.number_of_floors -= other
            return self

    def __mul__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors * other)
        elif isinstance(other, House):
            return House(self.name, self.number_of_floors * other.number_of_floors)
        else:
            print("Объекты должны быть класса House и int или оба объекта должны быть класса House.")
            return

    def __rmul__(self, other):
            return self * other

    def __imul__(self, other):
        if not isinstance(other, int):
            print("Правый операнд должен быть типом int или объектом House")
            return
        else:
            self.number_of_floors *= other
            return self

    def __truediv__(self, other):
        if isinstance(other, int) and other != 0 :
            return House(self.name, int(self.number_of_floors / other))
        elif isinstance(other, House) and other.number_of_floors != 0:
            return House(self.name, int(self.number_of_floors / other.number_of_floors))
        else:
            print("Классы объектов не совпадают или деление на ноль")
            return

    def __rtruediv__(self, other):
        if isinstance(other, int) and self.number_of_floors != 0:
            return House(self.name, int(other / self.number_of_floors))
        elif isinstance(other, House) and self.number_of_floors != 0:
            return House(self.name,  int(other.number_of_floors / self.number_of_floors))
        else:
            print("Классы объектов не совпадают или деление на ноль")
            return

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i + 1)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

h2 = h2 - 10 # __sub__
print(h2)
h2 = h2 - h1 # __sub__
print(h2)
h2 = 10 - h2 # __rsub__
print(h2)
h2 -= (-10) # __isub__
print(h2)

h2 = h2 / 10 # __div__
print(h2)
h2 = h2 / h1 # __div__
print(h2)
h2 = 10 / h2 # __rdiv__
print(h2)
h1 /= 2
print(h1)