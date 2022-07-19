with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n\n')

numbers = input.pop(0).split(',')

boards_setup = [value.split('\n') for value in input]

boards = []

for board_raw in boards_setup:
    board = []
    for row_raw in board_raw:
        row_split = row_raw.split(' ')
        row = []
        for value in row_split:
            if value != '':
                row.append(value)
        board.append(row)
    boards.append(board)

boards_mirror = [ [ ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'] ] for value in boards]

def check_for_winner():
    winner = None

    for board_ind, board in enumerate(boards_mirror):

        for row in board:
            if row.count('x') == 0:
                winner = board_ind
                return winner

        for i in range(5):
            populated = True
            for row in board:
                if row[i] == 'x':
                    populated = False
                    break
            if populated:
                winner = board_ind
                return winner

    return winner


called_numbers = []

for number in numbers:

    called_numbers.append(number)
    current_board = []

    for board_ind, board in enumerate(boards):
        current_board = board
        for row_ind, row in enumerate(board):
            for col_ind, value in enumerate(row):
                if value == number:
                    boards_mirror[board_ind][row_ind][col_ind] = number

    if check_for_winner() != None:

        winning_board = boards[check_for_winner()]
        winning_number = int(number)
        sum_of_unmarked = 0

        for row in winning_board:
            for value in row:
                if called_numbers.count(value) == 0:
                    sum_of_unmarked += int(value)
        answer = winning_number * sum_of_unmarked
        print(answer)
        break

