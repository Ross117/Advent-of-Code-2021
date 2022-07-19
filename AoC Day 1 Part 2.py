with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

increases = 0

for ind, value in enumerate(input):
    if ind > 0 and ind < (len(input) - 2):
        if (int(value) + int(input[ind + 1]) + int(input[ind + 2])) > (int(input[ind - 1]) + int(value) + int(input[ind + 1])):
            increases += 1

print(increases)
