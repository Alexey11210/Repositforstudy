class Vehicle:
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)
    __COLOR_VARIANTS = ['pink', 'blue', 'green', 'orange', 'white']
    def get_model(self):
        return (f'Модель: {self.__model}')
    def get_horsepower(self):
        return (f'Мощность двигателя: {self.__engine_power}')
    def get_color(self):
        return (f'Цвет: {self.__color}')
    def print_info(self):
        print(f'{Vehicle.get_model(self)},\n{Vehicle.get_horsepower(self)},\n{Vehicle.get_color(self)},\nВладелец: {self.owner}\n')
    def set_color(self, new_color):
        self.new_color = str(new_color)
        if new_color.lower() not in Vehicle.__COLOR_VARIANTS:
            print (f"Нельзя сменить цвет на {new_color}")
        else:
            self.__color = new_color

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()