import SelectionSort as sort

def countDuplicate(dataList, elem):
    count=0
    for e in dataList:
        if e != elem:
            return elem, count
        count +=1
    return elem, count
            
def compactList(alist):
    'return a list of tuples consisting of number and its frequency; [(num1, freq1), ...]'
    zipped=[]
    index=0
    while index < len(alist):
        couple = countDuplicate(alist[index:], alist[index])
        zipped.append(couple)
        index += couple[1]
    return zipped
