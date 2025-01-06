def  personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for elem in numbers:
        try:
            result += elem
        except TypeError:
            incorrect_data += 1
            print(f' Введены некорректные данные для сложения: {elem}')
    return result, incorrect_data

def calculate_average(numbers):
    try:
        result = personal_sum(numbers)
        return result[0] / (len(numbers) - result[1])
    except ZeroDivisionError:
        return '0 (ноль)'
    except TypeError:
        print(f'В numbers записан некорректный тип данных')

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
