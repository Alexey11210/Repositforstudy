import math

def test_function(asd):
    # global k
    k = asd * 2
    print(k)
    def inner_function(asd):
        nonlocal k
        k = asd**2
        if k % 2 == 0:
            print(k, "Я в области видимости функции test_function")
        else:
            print(k)
    inner_function(k)
test_function(5)
test_function(13)
inner_function(k) # Если вызывать вне тестовой функции вызывается ошибка - функция не определена