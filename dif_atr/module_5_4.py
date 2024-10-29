class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
       # print(args)
        print(kwargs)
        cls.houses_history.append(args[0])
        return object.__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
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
    def go_to(self, floor):
        if floor < 1 or floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(floor):
                print(i+1)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)