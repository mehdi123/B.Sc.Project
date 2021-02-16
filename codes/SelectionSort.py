def findMin(sublist):
    i=0
    minimum=sublist[0]
    index=0
    while i < len(sublist):
        if sublist[i] < minimum:
            index=i
            minimum=sublist[i]
        i+=1
    return index
            
def selectionSort(disarray):
    index=0
    while index < len(disarray)-1:
        j = findMin(disarray[index:])
        j+=index
        disarray[index], disarray[j] = disarray[j], disarray[index]
        index+=1
