'''Factorial function means to multiply 
a series of descending natural number 3! = 3 x 2 x 1  
Note: it is generally agreed that 0! = 1. 
It may seem funny that the multiplying no numbers 
together gets us 1, but it helps simplify a lot 
of equation.'''

'''non-tail recursion; 
waste more memory when n is big integer
such as 1,000,000.'''

def fact(n):
    if n <= 1:
        return n
    return n * fact(n-1)

'''tail recursion; save 
more stack frame even though the integer
is big such as 1,000,000'''

def fact_tail(n, ret = 1):
    if n <= 1:
        return ret
    return fact_tail(n-1,ret*n)

'''PERMUTATION: 
To find the number of ways k items can be order
in n times'''

def perm(n,k):
    numerator = fact_tail(n)
    denominator = fact_tail(n-k)
    return numerator / denominator

'''COMBINATION:
The number of ways to combine k items 
from a set of n'''

def comb(n,k):
    numerator = perm(n,k)
    denominator = fact_tail(k)
    return numerator / denominator
    

if __name__ == "__main__":
    
    '''Permutation:  
        How many ways can we award a 1st, 2nd and 3rd place prize 
        among 10 contestants?
        (Gold / Silver / Bronze)'''
    
    print "Permutation : ",perm(10,3)
    
    '''Combination:
       How many ways can I give 3 tin cans to 10 people? 
        '''
    
    print "combination : ",comb(10,3)