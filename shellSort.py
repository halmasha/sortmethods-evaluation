import random
from time import time
k =0   # comparisons
def shellSort(alist):
    size = len(alist)
    start =time()
    
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startPosition in range(sublistCount):
            gapInsertionSort(alist, startPosition, sublistCount)
        sublistCount = sublistCount // 2
    end = time()
    print(size," items sorted in ", (end- start)," seconds",k," comparisons were made")

def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        global k
        while position >= gap and \
              alist[position - gap].getDate() > currentValue.getDate():
            k +=1
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentValue

def printList(alist):
    count = 0
    for x in range(len(alist)):
        
        if count % 10 == 0:
            print()
        print("%10d" % alist[x].getDate(),alist[x].getMaxTemp(),alist[x].getMinTemp(), end = " ")
        count += 1
    


