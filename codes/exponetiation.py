##def exp_iter(x, n):
##    prod=1
##    signFlag=0
##    if n<0:
##        n=-n
##        signFlag=1
##    while n>0:
##        prod *= x
##        n-=1
##    if signFlag:
##        return 1.0/prod
##    return prod

mul=0
def exp_recursive_1(x, n):
    'a recursive function for exponentiation'
    if n%2 == 0:
        temp=exp_recursive_1(x, n/2)
        return temp*temp
def exp_recursive_2(x, n):
    'a recursive function for exponentiation'
    if n==1:
        return x
    if n%2 == 0:
        temp=exp_recursive_2(x, n/2)
        return temp*temp
    if n%2 == 1:
        temp=exp_recursive_2(x, (n-1)/2)
        return x*temp*temp
    

def exp_recursive(x, n):
    'a recursive function for exponentiation'
    global mul
    if n<0:
        return 1.0/exp_recursive(x, -n)
    if n==1:
        return x
    if n%2 == 0:
        temp=exp_recursive(x, n/2)
        mul+=1
        return temp*temp
    if n%2 == 1:
        temp = exp_recursive(x, (n-1)/2)
        mul+=2
        return x*temp*temp

if __name__=='__main__':
    print exp_recursive(2, -16)
    print mul