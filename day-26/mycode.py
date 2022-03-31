with open("file1.txt") as file_one:
    file_one_list = file_one.readlines()
    result_one = []
    for file_one_line in file_one_list:
        file_one_line_stripped = int(file_one_line.strip())
        result_one.append(file_one_line_stripped)
    print(result_one)

with open("file2.txt") as file_two:
    file_two_list = file_two.readlines()
    result_two = []
    for file_two_line in file_two_list:
        file_two_line_stripped = int(file_two_line.strip())
        result_two.append(file_two_line_stripped)
    print(result_two)

max_list_len = 0

result = []

if len(result_one) > len(result_two):
    for counter in result_one:
        if counter in result_two:
            result.append(counter)
else:
    for counter in result_two:
        if counter in result_one:
            result.append(counter)

# Write your code above 👆

print(result)
