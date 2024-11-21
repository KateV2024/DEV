# Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.

def undentify_digit(file):
    numbers = []
    with open("test.txt", "r") as file:
        for line in file:
            my_list = line.split(", ")
            for char in my_list:
                if char.isdigit():
                    num = int(char)
                    numbers.append(num)
                    if num % 2 == 0:
                        with open("result2.txt", "a") as file2:
                            file2.write(str(num))
                    else:
                        with open("result1.txt", "a") as file1:
                            file1.write(str(num))

    return numbers

file = "test.txt"
result = undentify_digit(file)
print(result)


