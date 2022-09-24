with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

opening_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']
incomplete = []

# open_chunks tells us what needs to be closed & should give order - last element appended should be closed first then work back

for line in input:

    open_chunks = []
    is_corrupt = False

    for char in line:

        if char in opening_chars:
            open_chunks.append(char)
        elif char == closing_chars[opening_chars.index(open_chunks[len(open_chunks) - 1])]:
            open_chunks.pop(len(open_chunks) - 1)
        else:
            is_corrupt = True
            break

    if not is_corrupt:

        chars_to_complete = []

        for open_chunk in open_chunks:
            chars_to_complete.append(closing_chars[opening_chars.index(open_chunk)])
       
        chars_to_complete.reverse()

        incomplete.append(chars_to_complete)

points_table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []

for lines in incomplete:
    score = 0
    for char in lines:
        score = (score * 5) + points_table[char]
    scores.append(score)

scores.sort()

print(scores[round(len(scores) * 0.5)])
