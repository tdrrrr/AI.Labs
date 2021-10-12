men = []
women = []
boat = "left"


def initialize(n):
    for i in range(n):
        men.append([i, "m", "left"])
        women.append([i, "w", "left"])


def verifyTransport(person1, person2):
    if(passedornot(person1) == True):
        return False
    if(passedornot(person2) == True):
        return False
    if(boat == "right"):
        return False
    if(person1[0] == person2[0]):
        return True
    if(person1[1] == "w"):
        if((men[person1[0]])[2] == "left"):
            for m in men:
                if(m[2] == "right"):
                    return False
    if (person2[1] == "w"):
        if ((men[person2[0]])[2] == "left"):
            for m in men:
                if m[2] == "right":
                    return False
    return True


def transport(person1, person2):
    if verifyTransport(person1, person2):
        person1[2] = "right"
        person2[2] = "right"


def passed_or_not(person):
    if person[2] == "left":
        return False
    return True


if __name__ == '__main__':
    initialize(3)
    transport(men[0], men[0])
    print(men)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
