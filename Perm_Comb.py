'''non-tail recursion; 
waste more memory when n is big integer
such as 1,000,000.'''
def fact(n):
    if n == 0:
        return n
    if n == 1:
        return 1
    return n * fact(n-1)

'''tail recursion; save 
more stack frame even thoug the integer
is big such as 1,000,000'''
def fact_tail(n, ret = 1):
    if n == 0:
        return 0
    if n == 1:
        return ret
    return fact_tail(n-1,ret*n)

'''PERMUTATION: 
To find the number of ways k items can be order
in n imtes'''

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
    
    print "Permutation : ",perm(10,3)
    print "combination : ",comb(10,3)