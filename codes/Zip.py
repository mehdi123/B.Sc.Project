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
        e, c = countDuplicate(alist[index:], alist[index])
        zipped.append((e,c))
        index += c
    return zipped
