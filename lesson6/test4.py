# Даны два файла произвольного типа. Поменять местами их содержимое.
# Файлы должны быть бинарного типа

with open("test1.bin", "wb") as file:
    file.writelines(
        [
            "Content of the first file\n".encode(),
            "1st file\n".encode()
        ]
)

with open("test2.bin", "wb") as file:
    file.writelines(
        [
            "Content of the second file\n".encode(),
            "2nd file\n".encode()
        ]
)

with open("test1.bin", "rb") as file:
    file1_content = []
    for line in file:
        line = line.decode()
        file1_content.append(line)
print(f"this is 1st file content: {file1_content}")

with open("test2.bin", "rb") as file:
    file2_content = []
    for line in file:
        line = line.decode()
        file2_content.append(line)
print(f"this is 2st file content: {file2_content}")

with open("test1.bin", "wb") as file:
    for line in file2_content:
        file.write(line.encode())

with open("test2.bin", "wb") as file:
    for line in file1_content:
        file.write(line.encode())

with open("test1.bin", "rb") as file:
    file1_content = []
    for line in file:
        line = line.decode()
        file1_content.append(line)
print(f"this is 1st file content: {file1_content}")

with open("test2.bin", "rb") as file:
    file2_content = []
    for line in file:
        line = line.decode()
        file2_content.append(line)
print(f"this is 2st file content: {file2_content}")