with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

input_cleaned = [value.split(' | ')[1].split(' ') for value in input]

unique_segments = 0

for values in input_cleaned:
    for signal in values:
        if len(signal) == 2 or len(signal) == 7 or len(signal) == 3 or len(signal) == 4:
            unique_segments += 1

print(unique_segments)
