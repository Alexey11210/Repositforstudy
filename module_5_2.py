class House:
    def  __init__(self, company_name, number_of_floors):
        self.name = company_name
        self.number_of_floors = number_of_floors
        print(f'Вас приветствует {self.name} Количество этажей: {self.number_of_floors}')
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > (self.number_of_floors):
            print(f'В {self.name} Такого этажа не существует')
        elif new_floor == (self.number_of_floors):
            print(f'Вас приветствует {self.name}, Ваш выбранный этаж:, {int(new_floor)} из {self.number_of_floors}')
        else:
            print(f'Вас приветствует {self.name}, Ваш выбранный этаж:, {int(new_floor)} из {self.number_of_floors}')
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Город 4212', 9)
h1.go_to(5)
h2.go_to(10)
h3.go_to(9)
print(len(h1))
print(len(h2))
print(h1)
print(h2)