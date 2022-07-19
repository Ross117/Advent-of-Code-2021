import numpy as np

def calc_fuel(distance):
    i = 0
    fuel = 0
    
    for num in range(distance):
        i += 1
        fuel += i

    return fuel

with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split(',')

input_cleaned = [int(value) for value in input]

alignment_pos = int(np.average(input_cleaned))

fuel_spent = 0

for crab in input_cleaned:
    distance = abs(crab - alignment_pos)

    fuel_spent += calc_fuel(distance)


print(fuel_spent)
