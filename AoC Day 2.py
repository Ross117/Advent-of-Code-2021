with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

tracker = {
    'horizontal': 0,
    'depth': 0,
    'aim': 0
}

split_input = []

for value in input:
    split_value = value.split(' ')
    split_input.append([split_value[0], int(split_value[1])])

for value in split_input:
    if value[0] == 'forward':
        tracker['horizontal'] += value[1]
        tracker['depth'] += tracker['aim'] * value[1]
    if value[0] == 'down':
        tracker['aim'] += value[1]
    if value[0] == 'up':
        tracker['aim'] -= value[1]

print(tracker['horizontal'] * tracker['depth'])
