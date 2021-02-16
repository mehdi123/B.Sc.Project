def Syracuse(n):
    if n==1:
        return 0
    if n%2==0:
        return Syracuse(n/2)
    return 1+Syracuse(3*n+1)
if __name__=='__main__':
    i=1
    while i<100000:
        print i,
#        raw_input()
        print Syracuse(i)
        i+=1
    
    
        