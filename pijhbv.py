calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    lenght = len(string)
    lower_case = string.lower()
    upprer_case = string.upper()
    return (lenght, lower_case, upprer_case)


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in list_to_search:
        if string == i.lower:
            return True
    return False


info = string_info("hello")
print(info)
contains = is_contains("Urban", ['ban', 'BaNaN', 'urBAN'])
print(contains)
contains = is_contains("cycle", ["recycling", 'cyclic'])
print(contains)
print(calls)