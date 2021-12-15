import random

DIMENSION = 4
directions = ['up', 'right', 'down', 'left']
epsilon = 0.9
discount = 0.9
learning_rate = 0.9


def find_man(board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            if (board[row])[column] == 'm':
                row_man = row
                column_man = column
    return row_man, column_man


def move_man(board, direction):
    row_man = (find_man(board))[0]
    column_man = (find_man(board))[1]
    if direction == 'up' and row_man - 1 >= 0:
        if (board[row_man - 1])[column_man] != 'i':
            print('move made')
            (board[row_man - 1])[column_man] = 'm'
            (board[row_man])[column_man] = 's'
    if direction == 'down' and row_man + 1 < DIMENSION:
        if (board[row_man + 1])[column_man] != 'i':
            print('move made')
            (board[row_man + 1])[column_man] = 'm'
            (board[row_man])[column_man] = 's'
    if direction == 'left' and column_man - 1 >= 0:
        if (board[row_man])[column_man - 1] != 'i':
            print('move made')
            (board[row_man])[column_man - 1] = 'm'
            (board[row_man])[column_man] = 's'
    if direction == 'right' and column_man + 1 < DIMENSION:
        if (board[row_man])[column_man + 1] != 'i':
            print('move made')
            (board[row_man])[column_man + 1] = 'm'
            (board[row_man])[column_man] = 's'
#  these functions were used for humans


def initialize_board_rewards(board, board_logic):
    board_row = []
    for row in board_logic:
        board_row = []
        for block in row:
            if block == 'm' or block == 's':
                board_row.append(-1)
            elif block == 'i':
                board_row.append(-100)
            else:
                board_row.append(100)
        board.append(board_row)


def print_board(board):
    for row in board:
        print(row)
    print('\n')


def generate_random_start():
    row, column = random.randint(0, 3), random.randint(0, 3)
    while verify_terminal_state(row, column):
        row, column = random.randint(0, 3), random.randint(0, 3)
    return row, column


def get_action(row, column, epsilon):
    nr = random.randint(1, 100) / 100
    if nr > epsilon:
        random_direction_index = random.randint(0, 3)
        return random_direction_index
    action_values = (board_Q[row])[column]
    return action_values.index(max(action_values))


def move(row, column, action):
    if action == 0 and row > 0:
        return row - 1, column
    if action == 1 and column < DIMENSION - 1:
        return row, column + 1
    if action == 2 and row < DIMENSION - 1:
        return row + 1, column
    if action == 3 and column > 0:
        return row, column - 1
    return row, column


def verify_terminal_state(row, column):
    return (board_rewards[row])[column] != -1


def reached_destination(row, column):
    return (board_rewards[row])[column] == 100


def train_ai(trials):

    for trial in range(trials):
        row, column = generate_random_start()

        while not verify_terminal_state(row, column):

            action = get_action(row, column, epsilon)
            #  we use the most rewarding action, or sometimes a random one

            old_row, old_column = row, column
            old_q_val = ((board_Q[old_row])[old_column])[action]
            #  we remember the previous stage information so that we can update it
            row, column = move(row, column, action)
            # we make the best known move so far 90% of the time (epsilon = 0.9)

            reward = (board_rewards[row])[column]
            td = reward + (discount * max((board_Q[row])[column])) - old_q_val
            #  the temporal difference is the difference between the move quality we knew and the actual reward
            #  with 0.9 * the best opportunity added

            new_q_value = old_q_val + (learning_rate * td)
            ((board_Q[old_row])[old_column])[action] = round(new_q_value, 2)
            #  we update the old_q_value with the new one


def get_shortest_path():
    row, column = generate_random_start()
    print('starting position: ', row, column)
    while not reached_destination(row, column):
        action = get_action(row, column, 1)
        print(directions[action])
        row, column = move(row, column, action)
        print(row, column)


def initialize_board_Q(board, board_logic):
    board_row = []
    for row in board_logic:
        board_row = []
        for block in row:
            board_row.append([0, 0, 0, 0])
        board.append(board_row)


if __name__ == '__main__':
    # m - man
    # s - safe zone
    # i - ice
    # r - reach point
    board_logic = [['m', 's', 's', 's'],
                   ['s', 'i', 's', 'i'],
                   ['s', 's', 's', 'i'],
                   ['i', 's', 's', 'r']]
    board_rewards = []
    board_Q = []
    initialize_board_rewards(board_rewards, board_logic)
    initialize_board_Q(board_Q, board_logic)
    print_board(board_logic)
    print_board(board_rewards)
    print_board(board_Q)
    train_ai(1000)
    print_board(board_Q)
    get_shortest_path()



    '''
    while True:
        direction = input('Choose direction(up, down, left, right) : ')
        if direction == 'quit':
            break
        move_man(board_logic, direction)
        print_board(board_logic)
    '''
