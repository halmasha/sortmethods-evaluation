
import csv
from insertionSort import  insertionSort
from binarySearch import binarySearch
import shellSort

class DayTemp():
    def __init__(self, date, maxTemp,minTemp):
        self.date = date
        self.minTemp = minTemp
        self.maxTemp = maxTemp
    def getDate(self):
        return self.date
    def getMinTemp(self):
        return self.minTemp
    def getMaxTemp(self):
        return self.maxTemp
     
    def getDay(self):  
        str1 = str(self.date)     
        return str1[6:]    
    def getYear(self):
        str1 = str(self.date)       
        return str1[:4]    
    def getMonth(self):
        str1 = str(self.date)        
        return str1[4:6]
    


date = []
minTemp = []
maxTemp  =[]
daysList2 = []
with open('Lawrence-KS.csv', newline='') as f:
    reader = csv.reader(f) 
     
    for row in reader:
        dayTemp = DayTemp(eval(row [0]),eval(row [1]),eval(row [2]))
        daysList2.append(dayTemp)
       
        
shellSort.shellSort(daysList2)
#shellSort.printList(daysList2)

def fahrConverter(temp):
    fahr = (temp/10) * 9/5 +32
    return round(fahr,2)
 
def getAverageTemp(alist):
    startYear = alist[0].getYear() #The earliest year in the record
    
    #The following variable hold sum of temperature for all days of a
    #in all the months from the first year in record to the last year
    jan = feb = mar = apr = may = jun = jul = aug = sep = octo = nov = dec = 0      
    size  = len(alist) # the size of the record list
    endYear = alist[size-1].getYear() # the last year in the record
    
    #The following values hold number of days for a given month in 
    #all the years in the record e.g n1 hold numbers of days whose temperature was 
    #recorded for every january  in the whole period recorded
    n1 = n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = n10 = n11 = n12 = 0
    for ind in range(size):
        month = int(alist[ind].getMonth())
        temp = fahrConverter(alist[ind].getMaxTemp())
        if month== 1:
            jan += temp
            n1 +=1
        if month == 2:
            feb += temp
            n2 +=1
            
        if month == 3:
            mar += temp
            n3 +=1
            
        if month == 4:
            apr += temp
            n4 +=1
            
        if month == 5:
            may += temp
            n5 +=1
            
        if month == 6:
            jun += temp
            n6 +=1
            
        if month == 7:
            jul += temp
            n7 +=1
            
        if month == 8:
            aug += temp
            n8 +=1
                        
        if month == 9:
            sep += temp
            n9 +=1
            
        if month == 10:
            octo += temp
            n10 +=1
       
        if month == 11:
            nov += temp
            n11 +=1
            
        if month == 12:
            dec += temp
            n12 +=1

    #Display
    print("Average Monthly Temperature recorded between ",startYear," to ", endYear)
    print("January: ",round((jan/n1),2)) 
    print("February: ",round((feb/n2),2)) 
    print("March: ",round((mar/n3),2)) 
    print("April: ",round((apr/n4),2)) 
    print("May: ",round((may/n5),2)) 
    print("June: ",round((jun/n6),2)) 
    print("July: ",round((jul/n7),2)) 
    print("August:",round((aug/n8),2)) 
    print("September: ",round((sep/n9),2)) 
    print("October: ",round((octo/n10),2)) 
    print("November: ",round((nov/n11),2)) 
    print("December: ",round((dec/n12),2))  
    
    #then we store the data in a external file for future reference    
    outfile = open("Average Monthly Temperature.txt", "w")
    outfile.write("Average Monthly Temperature recorded between "+str(startYear)+" to "+str(endYear))
    outfile.write("\nJanuary: "+str(round((jan/n1),2))) 
    outfile.write("\nFebruary: "+str(round((feb/n2),2))) 
    outfile.write("\nMarch: "+str(round((mar/n3),2)))
    outfile.write("\nApril: "+str(round((apr/n4),2))) 
    outfile.write("\nMay: "+str(round((may/n5),2))) 
    outfile.write("\nJune: "+str(round((jun/n6),2))) 
    outfile.write("\nJuly: "+str(round((jul/n7),2))) 
    outfile.write("\nAugust:"+str(round((aug/n8),2))) 
    outfile.write("\nSeptember: "+str(round((sep/n9),2))) 
    outfile.write("\nOctober: "+str(round((octo/n10),2))) 
    outfile.write("\nNovember: "+str(round((nov/n11),2))) 
    outfile.write("\nDecember: "+str(round((dec/n12),2)))  
            


def getTemperature():   
    date = input("\nEnter the date here: ")
    while date != "DONE":
        found = False            
        found, i = binarySearch(daysList2,eval(date))
        if found:
                print("The temperature for",date, "in fahrenheit degrees was; Max: ", fahrConverter(daysList2[i].getMaxTemp())
                      , ", min:", fahrConverter(daysList2[i].getMinTemp()))
                found = True        
        else:
            print("The temperature for that day is not in the record")        
        date = input("\nEnter the date here: ")
        

def main():    
    getAverageTemp(daysList2)
    getTemperature()  
main()

