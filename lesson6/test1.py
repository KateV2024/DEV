# Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить пустым.

def identify_digits(file):
    numbers = []

    with open(file, "r") as file:

        even_numbers = []
        odd_numbers = []

        for line in file:
            my_list = line.split(", ")
            for char in my_list:
                if char.isdigit():
                    num = int(char)
                    numbers.append(num)
                    if num % 2 == 0:
                        even_numbers.append(num)
                    else:
                        odd_numbers.append(num)

    with open("result2.txt", "w") as file2:
        file2.write(", ".join(map(str, even_numbers)) + "\n")

    with open("result1.txt", "w") as file1:
        file1.write(", ".join(map(str, odd_numbers)) + "\n")

    return numbers


file = "test.txt"
result = identify_digits(file)
print(", ".join(map(str, result)))
