with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split(',')

days = 0

def simulate(model):
    global days
    days += 1

    new_model = []

    for value in model:
        updated_value = apply_rules(value)
        if isinstance(updated_value, list):
            new_model.extend(updated_value)
        else: new_model.append(updated_value)

    if days == 80:
        return new_model
    else: 
        return simulate(new_model)

def apply_rules(value):
    if value == 0:
        new_value = [6, 8]
    else:
        new_value = (value - 1)

    return new_value

input_cleaned = [int(value) for value in input]

lanternfish = simulate(input_cleaned)

answer = len(lanternfish)

print(answer)
