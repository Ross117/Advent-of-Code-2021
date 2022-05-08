import numpy as np

with open('C:/Users/rmorran001/Documents/Python Scripts/Advent of Code/2021/Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split(',')

input_cleaned = [int(value) for value in input]

alignment_pos = int(np.median(input_cleaned))

fuel_spent = 0

for crab in input_cleaned:
    distance = abs(crab - alignment_pos)

    fuel_spent += distance

print(fuel_spent)