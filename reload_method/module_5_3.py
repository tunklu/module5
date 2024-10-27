class House:
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __eq__(self, other):
        return self.number_of_floors == other
    def __lt__(self, other):
        return self.number_of_floors < other
    def __le__(self, other):
        return self.number_of_floors <= other
    def __gt__(self, other):
        return self.number_of_floors > other
    def __ge__(self, other):
        return self.number_of_floors >= other
    def __ne__(self, other):
        return self.number_of_floors != other
    def __add__(self, value):
        if isinstance(self, House):
            if not isinstance(value, (int, House)):
                raise ArithmeticError("Правый операнд должен быть типом int или объектом House")
            floor = value if isinstance(value, int) else value.number_of_floors
            self.number_of_floors += floor
            return (self)
    def __radd__(self, value):
        if isinstance(self, House):
            if not isinstance(value, (int, House)):
                raise ArithmeticError("Правый операнд должен быть типом int или объектом House")
            floor = value if isinstance(value, int) else value.number_of_floors
            self.number_of_floors += floor
            return (self)
    def __iadd__(self, value):
        if isinstance(self, House):
            if not isinstance(value, (int, House)):
                raise ArithmeticError("Правый операнд должен быть типом int или объектом House")
            floor = value if isinstance(value, int) else value.number_of_floors
            self.number_of_floors += floor
            return (self)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, floor):
        if floor < 1 or floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(floor):
                print(i+1)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

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