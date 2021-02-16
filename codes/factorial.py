def factorial(n):
    'a recursive function for computing the factorial of n'
    if n<=1:
        return 1L
    return n*factorial(n-1)

if __name__=='__main__':
    print 10, factorial(10)
    print 20, factorial(20)
    print 400, factorial(40)
