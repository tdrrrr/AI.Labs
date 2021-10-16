import random

men = []
women = []
people = []
boat = "left"
nr_people_left = 0
nr_people_right = 0


def initialize(number_couples):
    global people
    for i in range(number_couples):
        men.append([i, "m", "left"])
        women.append([i, "w", "left"])
    people = men + women


def verify_if_done():
    for m in men:
        if m[2] == "left":
            return False
    for w in women:
        if w[2] == "left":
            return False
    return True


def verify_transport(person1, person2, side):
    #print(person1, person2, side)
    if passed_or_not(person1, side):
        #print("false1")
        return False

    if passed_or_not(person2, side):
        #print("false2")
        return False

    if boat == side:
        #print("false3")
        return False
    if person1[1] == "m":
        for w in women:
            if w != women[person1[0]]:
                if w[2] == side and (men[w[0]])[2] != side and person2[0] != w[0]:
                    #print("false3.1")
                    return False
    if person2[1] == "m":
        for w in women:
            if w != women[person2[0]]:
                if w[2] == side and (men[w[0]])[2] != side and person1[0] != w[0]:
                    #print("false3.2")
                    return False

    if person1[0] == person2[0] and (women[person1[0]])[2] == side:
        return True
    if person1[1] == "w":
        if person2[1] == men[person1[0]]:
            return True
        if (men[person1[0]])[2] != side:
            if person2[1] == "m" and person2 != men[person1[0]]:
                #print("false4")
                return False

            for m in men:
                if m[2] == side:
                    #print("false5")
                    return False

    if person2[1] == "w":
        if person1 == men[person2[0]]:
            return True
        if (men[person2[0]])[2] != side:
            if person1[1] == "m" and person1 != men[person2[0]]:
                #print("false6")
                return False

            for m in men:
                if m[2] == side:
                    #print("false7")
                    return False

    if person1[1] == "m":
        if (women[person1[0]])[2] == person1[2]:
            if person2[1] == "m":
                for m in men:
                    if m != men[person2[0]] and m != men[person1[0]]:
                        if m[2] != side:
                            #print("false8")
                            return False
            else:
                for m in men:
                    if m[2] != side:
                        #print("false9")
                        return False

    if person2[1] == "m":
        if (women[person2[0]])[2] == person2[2]:
            if person1[1] == "m":
                for m in men:
                    if m != men[person1[0]] and m != men[person2[0]]:
                        if m[2] != side:
                            #print("false10")
                            return False
            else:
                for m in men:
                    if m[2] != side:
                        #print("false11")
                        return False

    return True


def transport(person1, person2, side):
    global nr_people_right
    global nr_people_left
    global boat
    if verify_transport(person1, person2, side):
        print(str(person1[0]) + person1[1] + person1[2], str(person2[0]) + person2[1] + person2[2], " --> ", side)
        person1[2] = side
        person2[2] = side
        boat = side
        if person1[1] == "m":
            (men[person1[0]])[2] = side
        else:
            (women[person1[0]])[2] = side

        if person2[1] == "m":
            (men[person2[0]])[2] = side
        else:
            (women[person2[0]])[2] = side
        if person1 == person2:
            if side == "left":
                nr_people_left += 1
                nr_people_right -= 1
            else:
                nr_people_left -= 1
                nr_people_right += 1
        else:
            if side == "left":
                nr_people_left += 2
                nr_people_right -= 2
            else:
                nr_people_left -= 2
                nr_people_right += 2

        return True
    return False


def passed_or_not(person, side):
    if person[2] == side:
        return True
    return False


def great_right_move():
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                if transport(p1, p2, "right"):
                    return True
    return False


def average_right_move():
    for p1 in people:
        for p2 in people:
            if transport(p1, p2, "right"):
                return True
    return False


def great_left_move():
    for p1 in people:
        for p2 in people:
            if p1 == p2:
                if transport(p1, p2, "left"):
                    return True
    return False


def average_left_move():
    for p1 in people:
        for p2 in people:
            if transport(p1, p2, "left"):
                return True
    return False


def hillclimbing():
    global nr_people_left
    global people
    for i in range(25000):
        people = scrambled(people)
        print(nr_people_left)
        if not great_right_move():
            average_right_move()
        if not nr_people_left:
            break
        if not great_left_move():
            average_left_move()


def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest


def backtracking(peopleleft, peopleright, side):
    person = peopleleft.pop()
    if person is None:
        return True
    if side == 'left':
        side = 'right'
    else:
        side = 'left'
    for nextpers in peopleleft:
        if verify_transport(person, nextpers, side):
            peopleleft.remove(person)
            peopleright.append(nextpers)
            peopleright.append(person)
            if backtracking(peopleleft, peopleright, side):
                print('transport ', side, 'cu ', person, ' si ', nextpers)
    return False


def bfs(peopleleft, peopleright, side):
    person = peopleleft[0]

    if person is not None:
        if side == 'left':
            side = 'right'
        else:
            side = 'left'
        for nextpers in peopleleft:
            if verify_transport(person, nextpers, side):
                people.remove(person)
                peopleright.append(person, nextpers)
                print('transport ', side, 'cu ', person, ' si ', nextpers)
                break
        bfs(peopleleft, peopleright, side)


if __name__ == '__main__':
    n = input("Numarul de cupluri(1/2/3): ")
    n = int(n)
    nr_people_left = n * 2
    initialize(n)
    print(people)
    metoda = input("Metoda de rezolvare(Hillclimbing):")
    if metoda == "Hillclimbing":
        hillclimbing()
    print(people)