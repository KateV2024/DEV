# Написать функцию для факторила, генератор и рекурсию и сравнить время их работы

import time
import math


# Рекурсия

start_time = time.monotonic_ns()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

end_time = time.monotonic_ns()
rekursia_time = end_time - start_time
print(f"Время исполнения рекурсии в наносекундах: ", {rekursia_time})

# Импорт

start_time_import = time.monotonic_ns()

math.factorial(5)

end_time_import = time.monotonic_ns()
import_time_execution = end_time_import - start_time_import
print(f"Время исполнения импорта в наносекундах: ", {import_time_execution})

# Функция

start_time_func = time.monotonic_ns()

number = 5
def factorial(number):
    factorial = 1
    while number > 0:
        factorial *= number
        number = number - 1
    return factorial
result = factorial(number)
print(result)

end_time_func = time.monotonic_ns()
def_time_execution = end_time_func - start_time_func
print(f"Время исполнения функции в наносекундах: ", {def_time_execution})

# Генератор

start_time_gen = time.monotonic_ns()

def generator():
    factorial = 1
    for number in range(6):
            if number > 0:
                factorial *= number
            yield factorial

result_1 = generator()
print(next(result_1))
for number in result_1:
    print(number)


end_time_gen = time.monotonic_ns()
gen_time_execution = end_time_gen - start_time_gen
print(f"Время исполнения генератора в наносекундах: ", {gen_time_execution})

# Найти лучший результатов экзекьюшена

def best_result(result):
    return min(result)
best_time = best_result({gen_time_execution, import_time_execution, def_time_execution, rekursia_time})
print(f"Найлучшее время экзекьюшена", best_time)
