import random
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    count = 0
    ind = 0
    while first <= last and not found:
        count += 1
        midpoint = (first + last) // 2
        if alist[midpoint].getDate() == item:
            found = True
            ind = midpoint
        else:
            if item < alist[midpoint].getDate():
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found, ind

