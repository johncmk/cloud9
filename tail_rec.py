#tail-recursive function
'''Q: Why do you like functional programming so much?
        What does it acutally get you?
   A: tail recursion is its own reward'''

'''Simple tail recursion. Since the recursion call
at the end of the function. there is nothing left to do after
recursion is done. This optimizes the space in stack.'''

def print_rec(st):
    if len(st) == 0:
        return
    print st[0]
    print_rec(st[1:]) # tail recursive call

#non-tail-recursive-function

'''Although it looks like a tail recursive at first look. 
If we take a closer look, we can see that the value returned by fact(n-1) 
which is used in fact(n). Therefore, the call to fact(n-1) is
not the last thing done by fact(n)
(i.e.   1) fact(n-1)  ---> 2) n * result of fact(n-2). It reads from
right to left. Right function call first then multiply the result to the n)
the 2) is the last statement in the fuction therefore it is not 
tail recursion.'''

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

#from non-tail-recursive to tail-recursive above

'''The above function can be written as a tail recursive function.
The idea is to use one more argument and accumulate the factorial value 
in second argument. When n reaches 0, return the accumulated value.
(i.e 1)fact_tail(n-1,n*a) ) 
There is nothing left do to after the function is being called.'''

def fact_tail(n,a):
    if n == 0:
        return a
    return fact_tail(n-1,n*a)

#Compiler reads right to left

'''This function is to test that function calls primarily than a variable when
they are on the same line.'''

def right_to_left(st):
    print "right to left function called"
    return st

if __name__ == "__main__":
    
    st = "abcde"
    print_rec(st)
    
    n = 5
    print "non-tail factorial : ",fact(n)
    print "tail factorial : ",fact_tail(n,1)
    print "=========right to left test========="
    print "hello " + right_to_left("world") + " now"