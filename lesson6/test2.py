# Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного файла.
# Если чисел меньше 3 выводить ошибку

def find_four_digits(file):
    digits = []
    with open("test.txt", "r") as file:
        for line in file:
            my_list = line.split(", ")
            for char in my_list:
                if char.isdigit():
                    digits.extend(my_list)
        if len(digits) <= 3:
            return "error"
        else:
            return [digits[0], digits[1], digits[-2], digits[-1]]

file = "test.txt"
result = find_four_digits(file)
print(result)



