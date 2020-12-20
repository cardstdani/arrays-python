a = [41, 14, 6, 23, 19, 2, 11, 8, 30]

def quickSort(n):
    if len(n) < 2:
        return n

    pivot = n.pop()
    rightList = []
    leftList = []

    for item in n:
        if item > pivot:
            rightList.append(item)
        else:
            leftList.append(item)

    return quickSort(leftList) + [pivot] + quickSort(rightList)

a = quickSort(a)
print(a)
