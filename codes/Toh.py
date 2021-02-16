def toh(n):
    i=0
    n=1<<n
    print n
    for i in range(1,n):
        print 'Move top disc from', (i&i-1)%3+1, ((i|i-1)+1)%3+1

if __name__=='__main__':
    toh(20)