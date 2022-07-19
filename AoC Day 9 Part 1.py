import functools

with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

matrix = []

for element in input:
    row = [int(value) for value in element]
    matrix.append(row)

low_points = []
max_row_ind = len(matrix) - 1

for row_ind, row in enumerate(matrix):

    max_col_ind = len(row) - 1
    curr_row = row_ind
    nxt_row = row_ind + 1
    prev_row = row_ind - 1
    
    for col_ind, element in enumerate(row):

        curr_col = col_ind
        nxt_col = col_ind + 1
        prev_col = col_ind - 1

        if (curr_row == 0 and curr_col == 0):
            if element < matrix[nxt_row][curr_col] and element < matrix[curr_row][nxt_col]:
                low_points.append(element + 1)
        elif (curr_row == max_row_ind and curr_col == 0):
            if element < matrix[prev_row][curr_col] and element < matrix[curr_row][nxt_col]:
                low_points.append(element + 1)
        elif (curr_row == max_row_ind and curr_col == max_col_ind):
            if element < matrix[prev_row][curr_col] and element < matrix[curr_row][prev_col]:
                low_points.append(element + 1)
        elif (curr_row == 0 and curr_col == max_col_ind):
            if element < matrix[nxt_row][curr_col] and element < matrix[curr_row][prev_col]:
                low_points.append(element + 1)
        elif curr_col == 0:
            if element < matrix[prev_row][curr_col] and element < matrix[nxt_row][curr_col] and element < matrix[curr_row][nxt_col]:
                low_points.append(element + 1)
        elif curr_row == 0:
            if element < matrix[curr_row][prev_col] and element < matrix[nxt_row][curr_col] and element < matrix[curr_row][nxt_col]:
                low_points.append(element + 1)
        elif curr_col == max_col_ind:
            if element < matrix[curr_row][prev_col] and element < matrix[nxt_row][curr_col] and element < matrix[prev_row][curr_col]:
                low_points.append(element + 1)
        elif curr_row == max_row_ind:
            if element < matrix[curr_row][prev_col] and element < matrix[curr_row][nxt_col] and element < matrix[prev_row][curr_col]:
                low_points.append(element + 1)
        elif element < matrix[prev_row][curr_col] and element < matrix[nxt_row][curr_col] and element < matrix[curr_row][prev_col] and element < matrix[curr_row][nxt_col]:
            low_points.append(element + 1)

sum_of_risk = functools.reduce(lambda a, b: a + b, low_points)

print(sum_of_risk)
