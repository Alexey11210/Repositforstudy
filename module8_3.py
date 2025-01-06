class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(__vin)
        self.__numbers = self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, vin_number):
        self.__vin = vin_number
        if isinstance(vin_number, (str, float)):
            raise IncorrectVinNumber(f'Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number >= 9999999:
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        self.__numbers = numbers
        if isinstance(numbers, (int, float)):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')