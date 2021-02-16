import random as rnd
import time

def maxSubvector_1(X):
    maxsofar=0
    length=len(X)
    for i in range(length):
        for j in range(length):
            sum=0
            for k in range(i,j+1):
                sum+=X[k]
            maxsofar=max(sum, maxsofar)
    return maxsofar

def maxSubvector_2(X):
    maxsofar=0
    length=len(X)
    for i in range(length):
        sum=0
        for j in range(i,length):
            sum+=X[j]
            maxsofar=max(maxsofar, sum)
    return maxsofar

def maxSubvector_3(X):
    maxhere=0
    maxsofar=0
    for i in range(len(X)):
        maxhere = max(maxhere+X[i], 0)
        maxsofar = max(maxsofar, maxhere)
        
    return maxsofar

if __name__=='__main__':
    rlist=[rnd.randint(-10000,10000) for i in range(500)]
    t=time.time()
    print maxSubvector_1(rlist)
    t2=time.time()
    print t2-t
    print maxSubvector_2(rlist)
    print time.time()-t2
    print maxSubvector_3(rlist)