def intersect(A, B):
    result=[]
    if len(A)==0 or len(B)==0:
        return result
    for item in A:
        if item in B:
            result.append(item)
    return result
