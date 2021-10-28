cities = []


# city = [name, color, list of possible colors, list of neighbours]


def init_cities():
    global cities
    cities = [
        ['saveni', 'none', ['r', 'g', 'b'], ['botosani', 'iasi', 'trusesti', 'darabani', 'vaslui', 'baicoi', 'gogosari']],
        ['botosani', 'none', ['r', 'g', 'b'], ['iasi', 'saveni']],
        ['iasi', 'none', ['r', 'g', 'b'], ['botosani', 'saveni', 'trusesti']],
        ['trusesti', 'none', ['r', 'g', 'b'], ['iasi', 'saveni', 'darabani']],
        ['darabani', 'none', ['r', 'g', 'b'], ['trusesti', 'saveni', 'vaslui']],
        ['cosula', 'none', ['r', 'g', 'b'], []],
        ['vaslui', 'none', ['r', 'g', 'b'], ['saveni', 'darabani']],
        ['baicoi', 'none', ['r', 'g', 'b'], ['saveni', 'gogosari']],
        ['gogosari', 'none', ['r', 'g', 'b'], ['saveni', 'baicoi']],

    ]


def test_list():
    for city in cities:
        print(city)


def minimum_remaining_value():
    mrv = cities[0]
    index = 0
    for city in cities:
        if city[1] == 'none':
            mrv = city
            index = cities.index(city)
            break

    for city in cities:
        if city[1] == 'none':
            if len(city[2]) < len(mrv[2]):
                mrv = city
                index = cities.index(city)

    return index


def mrv_coloring():
    colored = 0
    while colored < len(cities):
        index = minimum_remaining_value()
        mrv_city = cities[index]
        print(mrv_city[0], mrv_city[2])
        mrv_city[1] = (mrv_city[2]).pop(0)
        print(mrv_city[1])
        for neighbor in mrv_city[3]:
            for city in cities:
                if city[0] == neighbor:
                    if mrv_city[1] in city[2]:
                        city[2].remove(mrv_city[1])
        colored += 1


if __name__ == '__main__':
    init_cities()
    #test_list()
    mrv_coloring()
    test_list()
