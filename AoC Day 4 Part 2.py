with open('C:/Users/rmorran001/Documents/Python Scripts/Advent of Code/2021/Input.txt', mode='r', encoding='utf-8') as file:
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

called_numbers = []
winning_boards = []
winning_numbers = []

def check_for_winner():

    for board in boards_mirror:

        if winning_boards.count(board) != 0:
            continue

        for row in board:
            if row.count('x') == 0:
                if winning_boards.count(board) == 0:
                    winning_boards.append(board)
                if winning_numbers.count(number) == 0:
                    winning_numbers.append(number)

        for i in range(5):
            populated = True
            for row in board:
                if row[i] == 'x':
                    populated = False
                    break
            if populated:
                if winning_boards.count(board) == 0:
                    winning_boards.append(board)
                if winning_numbers.count(number) == 0:
                    winning_numbers.append(number)


for number in numbers:
    
    called_numbers.append(number)
    current_board = []

    for board_ind, board in enumerate(boards):
        current_board = board
        for row_ind, row in enumerate(board):
            for col_ind, value in enumerate(row):
                if value == number:
                    boards_mirror[board_ind][row_ind][col_ind] = number

    check_for_winner()

        
winning_number = int(winning_numbers[len(winning_numbers) - 1]) 
sum_of_unmarked = 0
numbers_to_last_winner = called_numbers[0: (called_numbers.index(winning_numbers[len(winning_numbers) - 1])) + 1]

for row in winning_boards[len(winning_boards) - 1]:
    for value in row:
        if numbers_to_last_winner.count(value) == 0:
            sum_of_unmarked += int(value)

answer = winning_number * sum_of_unmarked

print(answer)


