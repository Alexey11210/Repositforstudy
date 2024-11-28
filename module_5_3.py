class House:
    def  __init__(self, company_name, number_of_floors):
        self.name = company_name
        self.number_of_floors = number_of_floors
        print(f'Вас приветствует {self.name} Количество этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if new_floor < 1 or new_floor > (self.number_of_floors):
                print(f'В "{self.name}" такого этажа не существует')
                break
            else:
                print(i)

    def __len__(self):
        return self.number_of_floors
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self
    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self
    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# print(h1)
# print(h2)
print(h1 == h2)
h1 = h1 + 10
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
