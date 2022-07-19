with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split(',')

lanternfish = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

input_cleaned = [int(value) for value in input]

# initial setup
for key in lanternfish:
    lanternfish[key] = input_cleaned.count(key)

days = 0

while days < 256:
    days += 1

    original_zeros = lanternfish[0]
    original_sevens = lanternfish[7]

    for i in range(9):
        if i == 6 or i == 8:
            pass
        else: lanternfish[i] = lanternfish[i + 1]

    lanternfish[6] = (original_sevens + original_zeros)
    lanternfish[8] = original_zeros

answer = 0

for key in lanternfish:
    answer += lanternfish[key]

print(answer)
