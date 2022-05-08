with open('C:/Users/rmorran001/Documents/Python Scripts/Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

numbers = [int(value) for value in input]

increases = 0

for ind, value in enumerate(numbers):
    if ind < (len(input) - 1):
        if numbers[ind + 1] > value:
             increases += 1