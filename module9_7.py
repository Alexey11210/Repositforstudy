def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 2:
            print("Составное")
            return result
        for i in range(2, result):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper

@ is_prime
def sum_three(*args):
    return sum(args)

res = sum_three(1,1,2)
print(res)
result = sum_three(2, 3, 6)
print(result)