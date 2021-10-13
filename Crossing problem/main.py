men = []
women = []
people = []
boat = "left"


def initialize(n):
    for i in range(n):
        men.append([i, "m", "left"])
        women.append([i, "w", "left"])


def verify_if_done():
    for m in men:
        if m[2] == "left":
            return False
    for w in women:
        if w[2] == "left":
            return False
    return True


def verify_transport(person1, person2, side):
    if passed_or_not(person1, side):
        return False
    if passed_or_not(person2, side):
        return False
    if boat == side:
        return False
    if person1[0] == person2[0]:
        return True
    if person1[1] == "w":
        if (men[person1[0]])[2] != side:
            if person2[1] == "m" and person2 != men[person1[0]]:
                return False
            for m in men:
                if m[2] == side:
                    return False
    if person2[1] == "w":
        if (men[person2[0]])[2] != side:
            if person1[1] == "m" and person1 != men[person2[0]]:
                return False
            for m in men:
                if m[2] == side:
                    return False
    if person1[1] == "m":
        if (women[person1[0]])[2] == person1[2]:
            return False
    if person2[1] == "m":
        if (women[person2[0]])[2] == person2[2]:
            return False
    return True


def transport(person1, person2, side):
    if verify_transport(person1, person2, side):
        print(str(person1[0]) + person1[1] + person1[2], str(person2[0]) + person2[1] + person2[2], " --> ", side, "\n")
        person1[2] = side
        person2[2] = side
        boat = side
        return True
    return False


def passed_or_not(person, side):
    if person[2] == side:
        return True
    return False

def backtracking( peopleleft , peopleright, side):
    person=peopleleft.pop()

    if person is None  :
        return True
    if side == 'left':
        side='right'
    else:
        side = 'left'
    for nextpers in peopleleft:
        if verify_transport(person, nextpers, side) == True :
            peopleleft.remove(person)
            peopleright.append(nextpers)
            peopleright.append(person)
            if backtracking(peopleleft,peopleright,side)==True:
                print('transport ',side,'cu ',person,' si ', nextpers)
    return False

def BFS( peopleleft , peopleright, side):
    person=peopleleft[0]

    if person is not None  :
        if (side == 'left'):
            side='right'
        else:
            side = 'left'
        for nextpers in peopleleft:
            if verify_transport(person, nextpers, side) == True :
                people.remove(person)
                peopleright.append(person,nextpers)
                print('transport ',side,'cu ',person,' si ', nextpers)
                break;
        BFS(peopleleft,peopleright,side)




if __name__ == '__main__':
    initialize(3)
    people = men + women
    print(people)
    transport(men[0], men[1], "right")
    print(men)
    print(women)
    
    #backtracking si bfs
    peopleleft=men+women
    peopleright = []
    side = 'left'
    backtracking(peopleleft,peopleright,side)
    BFS(peopleleft,peopleright,side)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
