import numpy as np

def calc_fuel(distance):
    i = 0
    feul = 0
    
    for num in range(distance):
        i += 1
        feul += i

    return feul

with open('C:/Users/rmorran001/Documents/Python Scripts/Advent of Code/2021/Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split(',')

input_cleaned = [int(value) for value in input]

alignment_pos = int(np.average(input_cleaned))

fuel_spent = 0

for crab in input_cleaned:
    distance = abs(crab - alignment_pos)

    fuel_spent += calc_fuel(distance)


print(fuel_spent)