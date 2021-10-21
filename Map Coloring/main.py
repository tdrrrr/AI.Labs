cities = []
# city = [name, colored or not, list of possible colors, list of neighbours]


def init_cities():
    global cities
    cities = [
        ['new york', False, ['r', 'g', 'b'], ['boston', 'new jersey']],
        ['botosani', False, ['g', 'b'], ['iasi', 'suceava', 'new york']],
        ['new jersey', False, ['r'], ['new york', 'boston']],
        ['boston', False, ['r', 'b'], ['new jersey', 'new york']]

    ]


def test_init():
    for city in cities:
        print(city)


if __name__ == '__main__':
    init_cities()
    test_init()
