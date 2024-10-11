immutable_var = 1, 'Валера', True, 19.5
print(immutable_var)
# immutable_var[2] = False Пытаемся изменить элементы кортежа.
# print(immutable_var) Кортеж не поддерживает обращение по элементам.
# Это нужно для того, чтобы в процессе работы случайно не изменить необходимый нам список.
mutable_list = ['Tree', 16, False, 1]
mutable_list[1] = 13.5
print(mutable_list)
mutable_list[2] = 'Camera'
print(mutable_list)
mutable_list[0:2] = 3, 4
print(mutable_list)