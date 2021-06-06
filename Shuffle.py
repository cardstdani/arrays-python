import random

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def shuffle(n):
    shuffledList = []
    unshuffledList = n

    for i in range(1, len(unshuffledList)):
        index = random.randint(0, len(unshuffledList) - 1)
        shuffledList.append(unshuffledList[index])
        del unshuffledList[index]
    shuffledList.insert(random.randint(0, len(shuffledList) - 1), unshuffledList[0])
    return shuffledList

a = shuffle(a)
print(a)
