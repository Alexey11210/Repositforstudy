# Словари
from time import sleep
my_dict = {'Valera' : '100 рублей',
           'Egor' : '250 рублей',
           'Andrey' : '320 рублей',
           'Gena' : '139 рублей'}
print(my_dict)
print(my_dict['Valera'])
print(my_dict.get('Anna'))
my_dict.update({'Alex' : '319 рублей',
                'Daniil' : '229 рублей'})
a = my_dict.pop('Andrey')
print(my_dict)
print(a)
sleep(2)
#
# Множества
my_set = {16,29,'Valera',17,45,14,16,29,17,'Valera'}
print(my_set)
my_set.add('Gennadiys')
print(my_set)
my_set.add(13.3)
print(my_set)
my_set.discard(29)
print(my_set)
