my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(len(my_list))
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
    if my_list[index] == 0:
        del my_list[index]
    if my_list[index] < 0:
        break