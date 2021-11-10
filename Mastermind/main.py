import random
from itertools import product


nr_of_colors = 0
states = []
available_balls = []
final_state = []
first_state = []
nr_of_moves = 0
move_number = 0
solution_nr_balls = 0
potential_solutions = []
potential_2x2_solutions = []


#TODO
# error when the input string does not match

def init(nr_colors, nr_balls_each_color, sequence_nr_balls):
    global nr_of_moves
    global available_balls
    global final_state
    global nr_of_colors
    global solution_nr_balls
    solution_nr_balls = sequence_nr_balls
    nr_of_colors = nr_colors
    nr_of_moves = nr_colors * 2
    available_balls = list(range(nr_colors)) * nr_balls_each_color
    final_state = random_state(sequence_nr_balls)
    return final_state


def generate_all_solutions():
    global potential_solutions
    global potential_2x2_solutions
    potential_solutions_tuples = list(product(range(nr_of_colors), repeat=solution_nr_balls))
    potential_solutions = [list(elem) for elem in potential_solutions_tuples]
    for solution in potential_solutions:
        if solution[0] == solution[1] and solution[2] == solution[3]:
            potential_2x2_solutions.append(solution)
    print(potential_2x2_solutions)


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


def play_ai():
    local_potential_solutions = potential_solutions
    turn = 0
    rnd = potential_2x2_solutions[random.randint(0, len(potential_2x2_solutions)-1)]
    turn += 1
    print('Turn #', turn)
    print(rnd)
    while compare(rnd, final_state) == 0:
        turn += 1
        print('Turn #', turn)
        print(rnd)
        rnd = potential_2x2_solutions.pop(random.randint(0, len(potential_2x2_solutions)-1))
    while compare(rnd, final_state) != 4:
        turn += 1
        print('Turn #', turn)
        for potential_solution in local_potential_solutions:
            if compare(potential_solution, rnd) != compare(rnd, final_state):
                local_potential_solutions.remove(potential_solution)
        max_score = 0
        rnd_candidate = local_potential_solutions[0]
        for potential_solution in local_potential_solutions:
            score = 0
            for solution in potential_solutions:
                    score += compare(potential_solution, solution)
            if score > max_score:
                max_score = score
                rnd_candidate = potential_solution
        rnd = rnd_candidate
        print(rnd)
    return rnd


if __name__ == '__main__':
    print(init(6, 4, 4))
    print(available_balls)
    generate_all_solutions()
    print(len(potential_solutions))
    print(play_ai())
    #play()


