# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.

def find_squared_numbers(file):
    squared_numbers = []
    with open("test.txt", "r") as file:
        for line in file:
            my_list = line.split(", ")
            for char in my_list:
                if char.isdigit():
                    num = int(char)
                    squared_numbers.append(num ** 2)
    return squared_numbers



file = "test.txt"
result = find_squared_numbers(file)
print(result)

with open("test.txt", "w") as file:
    file.write(", ".join(map(str, result)))