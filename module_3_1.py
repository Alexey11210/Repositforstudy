calls = 0

def string_info(string):
    global info
    info = len(string), string.upper(), string.lower()
    print(info)
(string_info('capybara'))
(string_info('Armageddon'))
(string_info('Antapka'))


def is_contains(string, list_to_search):
    global nancy
    nancy = True
    if string.lower() in list_to_search:
        print(nancy)
    else:
        nancy = False
print(is_contains('Urban', ['ban', 'BaNaN', ('urBAN'.lower())]))
print(is_contains('cycle', ['recycling', 'cyclic']))


def count_calls(calls):
    global calls
    if info:
        calls += 1
    elif nancy:
        calls += 1
print(calls)
