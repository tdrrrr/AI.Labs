DIMENSION = 4


def find_man(board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            print(row, column)
            if (board[row])[column] == 'm':
                row_man = row
                column_man = column
    return row_man, column_man


def move_man(board, direction):
    ice_there = False
    out_of_bounds = False
    row_man = (find_man(board))[0]
    column_man = (find_man(board))[1]
    if direction == 'up' and row_man - 1 >= 0:
        if (board[row_man - 1])[column_man] != 'i':
            (board[row_man - 1])[column_man] = 'm'
            (board[row_man])[column_man] = 's'
    if direction == 'down' and row_man + 1 <= DIMENSION:
        if (board[row_man + 1])[column_man] != 'i':
            (board[row_man + 1])[column_man] = 'm'
            (board[row_man])[column_man] = 's'
    if direction == 'left' and column_man - 1 >= 0:
        if (board[row_man])[column_man - 1] != 'i':
            (board[row_man])[column_man - 1] = 'm'
            (board[row_man])[column_man] = 's'
    if direction == 'right' and column_man + 1 >= DIMENSION:
        print(row_man, column_man)
        if (board[row_man])[column_man + 1] != 'i':
            (board[row_man])[column_man + 1] = 'm'
            (board[row_man])[column_man] = 's'


def print_board(board):
    for row in board:
        print(row)
    print('\n')


if __name__ == '__main__':
    # m - man
    # s - safe zone
    # i - ice
    # r - reach point
    board_logic = [['m', 's', 's', 's'],
                   ['s', 'i', 's', 'i'],
                   ['s', 's', 's', 'i'],
                   ['i', 's', 's', 'r']]
    print_board(board_logic)
    while True:
        direction = input('Choose direction(up, down, left, right) : ')
        if direction == 'quit':
            break
        move_man(board_logic, direction)
        print_board(board_logic)
