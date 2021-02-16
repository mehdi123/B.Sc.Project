def reverse1(theList):
    rindex=len(theList)-1
    for index in range(len(theList)/2):
        theList[index], theList[rindex] = theList[rindex], theList[index]
        rindex-=1
def reverse2(theList):
    length=len(theList)
    rindex=length-1
    index=0
    while index<length/2:
        theList[index], theList[rindex] = theList[rindex], theList[index]
        rindex-=1
        index+=1
        