import random
from time import time
def insertionSort(alist):
    size = len(alist)
    start =time()
    k =0   # comparisons
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index
        while position > 0 and alist[position - 1].getDate() > currentValue.getDate():
            alist[position] = alist[position - 1]
            position = position - 1
            k +=1
        alist[position] = currentValue
    end = time()
    print(size," items sorted in ", (end- start)," seconds",k," comparisons were made")
    
def printList(alist):
    count = 0
    for x in range(len(alist)):
                
        if count % 10 == 0:
            print()        
        print(format(str(alist[x][0])+" "+str(alist[x][1])+" "+str(alist[x][2]),"10s")+" ", end="")
        count += 1


