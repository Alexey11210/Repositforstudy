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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Город 4212', 6)
h1.go_to(5)
h2.go_to(10)
h3.go_to(6)
