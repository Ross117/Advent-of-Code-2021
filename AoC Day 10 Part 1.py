with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

opening_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']

illegal_chars = []

for line in input:

    open_chunks = []

    for char in line:

        if char in opening_chars:
            open_chunks.append(char)
        elif char == closing_chars[opening_chars.index(open_chunks[len(open_chunks) - 1])]:
            open_chunks.pop(len(open_chunks) - 1)
        else:
            # if char not closing char for latest_open_chunk - link is corrupt
            illegal_chars.append(char)
            break

points_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0

for illegal_char in illegal_chars:
    score += points_table[illegal_char]

print(score)
