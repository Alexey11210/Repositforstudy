calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    info = len(string), string.upper(), string.lower()
    print(info)
def is_contains(string, list_to_search):
    count_calls()
    nancy = True
    if string.lower() in list_to_search:
        print(nancy)
    else:
        nancy = False
        print(nancy)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', ('urBAN'.lower())]))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
