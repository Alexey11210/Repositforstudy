def add_everything_up(a, b):

    try:
        res = a + b
    except TypeError:
        print(str(a) + str(b))
    else:
        print(res)
    finally:
        print('Конец!')

(add_everything_up(123.456, 'строка'))
(add_everything_up('яблоко', 4215))
(add_everything_up(123.456, 7))