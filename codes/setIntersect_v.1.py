def isMemeberOf(set, item):
    index=0
    while index<len(set):
        if item==set[index]:
            return 1
        index+=1
    return 0

def intersect(A, B):
    result=[]
    if len(A)==0 or len(B)==0:
        return result
    index=0
    while index<len(A):
        item=A[index]
        if isMemeberOf(B, item)==1:
            result.append(item)
        index+=1
    return result

