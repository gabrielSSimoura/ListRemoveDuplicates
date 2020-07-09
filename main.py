# Write a program (function!) that takes a list # and returns a new
# list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list,
#  and another using sets.
# Go back and do Exercise 5 using sets,
# and write the solution for that in a different function.

import random


def generateRandomList():
    randomlist = []
    for i in range(0, 20):
        n = random.randint(1, 30)
        randomlist.append(n)

    return randomlist


def main():
    randomList = generateRandomList()
    print("Random List")
    print(randomList)

    randomList = set(randomList)
    randomList = list(randomList)

    print("Filtered List")
    print(randomList)


main()
