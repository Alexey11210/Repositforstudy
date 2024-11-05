def print_params(a = 1, b = 'строка', c = True):
    nancy = [a, b, c]
    print(nancy)
print_params(2,'Valera')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

value_list = [16, 14.3, 'Holland']
value_dict = {'a': 1924, 'b': 'April', 'c': 3.14}
print_params(*value_list)
print_params(**value_dict)
values_list_2 = ['Anbka', 1]
print_params(*values_list_2, 42)