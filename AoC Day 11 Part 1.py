with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

matrix = [[int(elem) for elem in value] for value in input]
total_flashes = 0

flashed = set()

# recursion with any_flashes as the break clause
def flash_cycle():
    global total_flashes
    any_flashes = False
    
    for row_ind, row in enumerate(matrix):
        for octopus_ind, octopus in enumerate(row):

            id = str(row_ind) + str(octopus_ind)

            if octopus > 9 and id not in flashed:
                # flash, register as flashed & reset to 0
                any_flashes = True
                total_flashes += 1
                matrix[row_ind][octopus_ind] = 0
                flashed.add(id)

                adj_offsets = [[row_ind - 1, octopus_ind - 1], [row_ind - 1, octopus_ind], [row_ind - 1, octopus_ind + 1], [row_ind, octopus_ind - 1], [row_ind, octopus_ind + 1], [row_ind + 1, octopus_ind - 1], [row_ind + 1, octopus_ind], [row_ind + 1, octopus_ind + 1]]

                # energy level of adjacent octopuses increased by 1
                for offsets in adj_offsets:
                    ind_a = offsets[0]
                    ind_b = offsets[1]

                    if str(ind_a) + str(ind_b) not in flashed and ind_a != -1 and ind_b != -1:
                        try:
                            matrix[ind_a][ind_b] += 1
                        except IndexError:
                            continue

    if not any_flashes:
        return

    flash_cycle()


def step():

    for row_ind, row in enumerate(matrix):
        for octopus_ind, octopus in enumerate(row):
             matrix[row_ind][octopus_ind] += 1

    flash_cycle()

    global flashed
    flashed = set()


for i in range(100):
    step()

print(total_flashes)
