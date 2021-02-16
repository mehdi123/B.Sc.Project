import compact
import SelectionSort as sorter
import random

def findMax(data):
    'finds the maximum in a list'
    
    maximum=0
    for d in data:
        if maximum < d:
            maximum=d
    return maximum

def printLine(freq,maximum):
    'is called for each line and print star or space character'
    
        index=0
        while index<len(freq):
            if freq[index] == maximum:
                freq[index] -= 1
                print '*',
            else:
                print ' ',
            index += 1
        print

def verticalHistogram(symbols, freq):
    'find maximum in the frequncies in each level and call printLine'
    
    m=findMax(freq)
    while m>0:
        printLine(freq,m)
        m=findMax(freq)
    for s in symbols:
        print s,
    print

def main(alist):
    'main function for combining the implemented functions'
    
    sorter.selectionSort(alist)
    zipped=compact.compactList(alist)
    symbols=[]s
    frequency=[]
    for(i,j)in zipped:
        symbols.append(i)
        frequency.append(j)
    verticalHistogram(symbols, frequency)

if __name__=='__main__':
    
    data=[]
    for i in range(50):
        data.append(random.randint(0,9))    #generating random numbers.
    main(data)
