import random

# numbers = [5, 8, 1, 4, 7]
numbers = [5, 8, 1, 4, 7, 3, 11, 10]


def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        random.shuffle(values)
        attempts += 1
    return values, attempts


print(bogo_sort(numbers))
