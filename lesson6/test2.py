# Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку

def find_four_gigits(file):
    digit = []
    with open("test.txt", "r") as file:
        for line in file:
            for char in line:
                if char.isdigit():
                    digit.append(char)
                    if len(digit) == 4:
                        return digit
    return "error"

file = "test.txt"
result = find_four_gigits(file)
print(result)



