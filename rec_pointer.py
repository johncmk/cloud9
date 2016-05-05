'''
Updating the el in the li while
traversing in recursion can effect the
changes of original value of the li in running time because
its updating the value via address.

Updating the value that is pass by value
through recursion would not change the orginal value
beause it copies the value before it goes into the
next stack frame
'''


def foo(x,n=3):
    if n == 0:
        return 0
    a = foo(x,n-1)
    b = foo(x,n-1)
    x = max(x, a+b)
    return x

def foo_li(li,n=3):
    if n == 0:
        return 0
    a = foo_li(li,n-1)
    b = foo_li(li,n-1)
    li[0] = max(li[0], a+b)
    return li[0]
    
if __name__ == "__main__":
    
    li = [5,4,3,2,1]
    
    print foo(1)
    # >> 4
    print foo_li([1])
    # >> 6