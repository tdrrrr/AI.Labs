import math


def read_from_file(filename):
    f = open(filename, "r")
    return f.read()


def sigmoid_function(x):
    return math.exp(x) / (math.exp(x) + 1)


def param_read():
    nr_max_epochs = input("Maximum number of epochs: ")
    learning_rate = input("Learning rate: ")
    vector_of_parameters = [nr_max_epochs, learning_rate]
    return vector_of_parameters


if __name__ == '__main__':
    print(read_from_file("input.txt"))
    print(sigmoid_function(2))
