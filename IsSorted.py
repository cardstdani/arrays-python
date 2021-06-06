array = [17, 4, 12, 45]

def isSorted(n):
    lastNumber = n[0]
    for i in range(0, len(n)):
        if (n[i] >= lastNumber):
            lastNumber = n[i]
        else:
            return False
    return True

print(isSorted(array))
