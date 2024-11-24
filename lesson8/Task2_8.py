# Напишите декоратор, который проверял бы тип параметров функции,
# конвертировал их если надо и складывал

def typed(func):
    def wrapper(a, b):
        a = str(a)
        b = str(b)
        return func(a, b)
    return wrapper

@typed
def add_two_symbols(a, b):
    return a + b

print(add_two_symbols("3", 5))  # "35"
print(add_two_symbols(5, 5))    # "55"
print(add_two_symbols("a", "b")) # "ab"

def typed(func):
    def wraper(a, b, c):
        a = float(a)
        b = float(b)
        c = float(c)
        return func(a, b, c)
    return wraper

@typed
def add_three_symbols(a,b,c):
    return a + b + c

print(add_three_symbols(5, 6, 7)) # 18
print(add_three_symbols("3", 5, 0)) # 8
print(add_three_symbols(0.1, 0.2, 0.3)) # 0.7000000001 ??
    
