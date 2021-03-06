import numpy as np

def create_2d_list(value):
    """
    Creates a 2-dimensional list from
    a string representinga a set of
    coordinates
    """
    
    one_dim = value.split(' -> ')
    two_dim = [value.split(',') for value in one_dim]

    return two_dim

def get_coordinates(val1, val2):
    """
    Gets all the numbers in a range,
    given the 2 end points.
    Returns the range in a list.
    """

    start = val1 if val1 < val2 else val2
    end = val1 if val1 > val2 else val2

    diff = end - start

    coordinates = [start]
    increment = start

    for i in range(diff):
        increment += 1
        coordinates.append(increment)

    if val1 > val2:
        coordinates.reverse()

    return coordinates

def update_matrix(moving_coords, static_coord, direction):
    """
    increment by 1 the number held at the matrix
    index specified by the given coordinates
    """

    for coord in moving_coords:
        if direction == "vertical":
            matrix[static_coord][coord] += 1
        elif direction == "horizontal":
            matrix[coord][static_coord] += 1

def update_matrix_diagonal(moving_coords_x, moving_coords_y):
    """
    increment by 1 the number held at the matrix
    index specified by the given coordinates
    """

    for ind, coord_x in enumerate(moving_coords_x):
        matrix[coord_x][moving_coords_y[ind]] += 1

def count_overlaps():
    """
    count the number of values in the
    matrix which are equal to or greater
    than 2
    """

    counter = 0

    for lst in matrix:
        for value in lst:
            if value >= 2:
                counter += 1

    return counter


with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

input_cleaned = [create_2d_list(value) for value in input]

matrix = np.zeros((1000, 1000), dtype=int)

for value in input_cleaned:

    x1, y1 = value[0]
    x2, y2 = value[1]
 
    if x1 == x2:
        moving_coords = get_coordinates(int(y1), int(y2))
        static_coord = int(x1)
        direction = "vertical"
        update_matrix(moving_coords, static_coord, direction)
    elif y1 == y2:
        moving_coords = get_coordinates(int(x1), int(x2))
        static_coord = int(y1)
        direction = "horizontal"
        update_matrix(moving_coords, static_coord, direction)
    else:
        moving_coords_x = get_coordinates(int(x1), int(x2))
        moving_coords_y = get_coordinates(int(y1), int(y2))
        update_matrix_diagonal(moving_coords_x, moving_coords_y)

answer = count_overlaps()

print(answer)
