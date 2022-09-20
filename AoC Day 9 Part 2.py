with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

matrix = []
dict = {}

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
            dict[curr_row, curr_col] = {'val': matrix[curr_row][curr_col], 'path': [[nxt_row, curr_col], [curr_row, nxt_col]]}
            if element < matrix[nxt_row][curr_col] and element < matrix[curr_row][nxt_col]:
                low_points.append([curr_row, curr_col])
        elif (curr_row == max_row_ind and curr_col == 0):
            dict[curr_row, curr_col] = {'val': matrix[curr_row][curr_col], 'path': [[prev_row, curr_col], [curr_row, nxt_col]]}
            if element < matrix[prev_row][curr_col] and element < matrix[curr_row][nxt_col]:
                low_points.append([curr_row, curr_col])
        elif (curr_row == max_row_ind and curr_col == max_col_ind):
            dict[curr_row, curr_col] = {'val': matrix[curr_row][curr_col], 'path': [[prev_row, curr_col], [curr_row, prev_col]]}
            if element < matrix[prev_row][curr_col] and element < matrix[curr_row][prev_col]:
                low_points.append([curr_row, curr_col])
        elif (curr_row == 0 and curr_col == max_col_ind):
            dict[curr_row, curr_col] = {'val': matrix[curr_row][curr_col], 'path': [[nxt_row, curr_col], [curr_row, prev_col]]}
            if element < matrix[nxt_row][curr_col] and element < matrix[curr_row][prev_col]:
                low_points.append([curr_row, curr_col])
        elif curr_col == 0:
            dict[curr_row, curr_col] = {'val': matrix[curr_row][curr_col], 'path': [[prev_row, curr_col], [nxt_row, curr_col], [curr_row, nxt_col]]}
            if element < matrix[prev_row][curr_col] and element < matrix[nxt_row][curr_col] and element < matrix[curr_row][nxt_col]:
                low_points.append([curr_row, curr_col])
        elif curr_row == 0:
            dict[curr_row, curr_col] = {'val': matrix[curr_row][curr_col], 'path': [[curr_row, prev_col], [nxt_row, curr_col], [curr_row, nxt_col]]}
            if element < matrix[curr_row][prev_col] and element < matrix[nxt_row][curr_col] and element < matrix[curr_row][nxt_col]:
                low_points.append([curr_row, curr_col])
        elif curr_col == max_col_ind:
            dict[curr_row, curr_col] = {'val': matrix[curr_row][curr_col], 'path': [[curr_row, prev_col], [nxt_row, curr_col], [prev_row, curr_col]]}
            if element < matrix[curr_row][prev_col] and element < matrix[nxt_row][curr_col] and element < matrix[prev_row][curr_col]:
                low_points.append([curr_row, curr_col])
        elif curr_row == max_row_ind:
            dict[curr_row, curr_col] = {'val': matrix[curr_row][curr_col], 'path': [[curr_row, prev_col], [curr_row, nxt_col], [prev_row, curr_col]]}
            if element < matrix[curr_row][prev_col] and element < matrix[curr_row][nxt_col] and element < matrix[prev_row][curr_col]:
                low_points.append([curr_row, curr_col])
        elif 1 == 1:
            dict[curr_row, curr_col] = {'val': matrix[curr_row][curr_col], 'path': [[prev_row, curr_col], [nxt_row, curr_col], [curr_row, prev_col], [curr_row, nxt_col]]}
            if element < matrix[prev_row][curr_col] and element < matrix[nxt_row][curr_col] and element < matrix[curr_row][prev_col] and element < matrix[curr_row][nxt_col]:
                low_points.append([curr_row, curr_col])

visited = []
basin_size = 1

def get_basin_size(start, start_paths):

    for path in start_paths:

        start_val = dict[start[0], start[1]]['val']
        path_val = dict[path[0], path[1]]['val']
        
        if path_val > start_val and path_val != 9 and path not in visited:
            global basin_size
            basin_size += 1
            visited.append(path)
            get_basin_size(path, dict[path[0], path[1]]['path'])

    return

basin_sizes = []

for low_point in low_points:
    get_basin_size(low_point, dict[low_point[0], low_point[1]]['path'])
    basin_sizes.append(basin_size)
    basin_size = 1

basin_sizes.sort(reverse=True)

answer = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

print(dict)