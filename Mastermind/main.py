import random
nr_of_colors = 0
states = []
available_balls = []
final_state = []
first_state = []
nr_of_moves = 0
move_number = 0


#TODO
# make the game recognize the right state when the compare function returns 4
# error when the input string does not match

def init(nr_colors, nr_balls_each_color, sequence_nr_balls):
    global nr_of_moves
    global available_balls
    global final_state
    global nr_of_colors
    nr_of_colors = nr_colors
    nr_of_moves = nr_colors * 2
    available_balls = list(range(nr_colors)) * nr_balls_each_color
    final_state = random_state(sequence_nr_balls)
    return final_state


def random_state(sequence_nr_balls):
    state = []
    available_balls_first_state = available_balls.copy()
    for index_ball in range(sequence_nr_balls):
        state.append(available_balls_first_state.pop(random.randint(0, len(available_balls_first_state)-1)))
    return state


def compare(state_one, state_two):
    positional_occurence = 0
    for index in range(0, len(state_one)):
        if state_one[index] == state_two[index]:
            positional_occurence += 1
    return positional_occurence


def verify_state(state):
    return state == final_state


def play():
    while len(states) < nr_of_moves:
        state_int = []
        state = input('Choose the BALLS: ')
        for number in state:
            state_int.append(int(number))
        for number in state_int:
            if number > nr_of_colors:
                print('Eroare la insertie, culoare inexistenta sau format gresit')
                continue
        if compare(state_int, final_state) == 4:
            print('You Won!')
            break
        states.append(state_int)
        print('You got ', compare(state_int, final_state), 'BALL/S correct')
        print(states)
    if len(states) == nr_of_moves:
        print('You yeed your last haw, GAME OVER!')


if __name__ == '__main__':
    print(init(5, 2, 4))
    print(available_balls)
    test = [1, 2, 3, 4]
    print(compare(test, final_state))
    play()


