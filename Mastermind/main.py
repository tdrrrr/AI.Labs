import random

colors = ['red', 'blue', 'yellow', 'purple', 'orange', 'green', 'brown', 'white', 'black', 'grey', 'pink']
available_balls = []
final_state = []
first_state = []
nr_of_moves = 0
move_number = 0

def init(nr_colors, nr_balls_each_color, sequence_nr_balls):
    global nr_of_moves
    nr_of_moves = nr_colors * 2
    for index_color in range(nr_colors):
        for index_nr_balls in range(nr_balls_each_color):
            available_balls.append(colors[index_color])
    available_balls_first_state = available_balls
    for index_ball in range(sequence_nr_balls):
        final_state.append(available_balls_first_state.pop(random.randint(0, len(available_balls))))
    return first_state


def random_state(sequence_nr_balls):
    available_balls_first_state = available_balls
    for index_ball in range(sequence_nr_balls):
        final_state.append(available_balls_first_state.pop(random.randint(0, len(available_balls))))
    return final_state


def verify_state(state):
    if nr_of_moves >= move_number:
        return 'player 1'
    return 'player 2' if state == final_state else 'player 1'


if __name__ == '__main__':
    init(5, 2, 4)
