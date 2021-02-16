def intersect(A, B):
    if len(A)==0 or len(B)==0:
        return []
    return [item for item in A if item in B]

