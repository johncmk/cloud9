class Tree:
    
    __slots__ = "root,left,right".split()
    
    def __init__(self, root = None, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right
        
'''preorder'''
def print_t(t,tab=1):
    if t is None:
        return
    print '\t'*tab, t.root
    print_t(t.left,tab+1)
    print_t(t.right,tab+1)


'''
Using the dictionary
'''
def find_dic(t,x, d={}):
    if t is None:
        key = min(d)
        return d[key]
    
    l = t.left
    rt = t.root
    r = t.right
    
    el = abs(rt-x)
    d[el] = rt
    if x == rt:
        return x 
    if x < rt:
        return find_dic(t.left,x,d)
    if x > rt:
        return find_dic(t.right,x,d)

'''
Without using the dictionary
'''
import sys

# returns the mininum distance between two node 
def _min(n1,n2,x):
    d1 = abs(n1-x)
    d2 = abs(n2-x)
    if d1 < d2:
        return n1
    return n2

def find(t,x,dm=sys.maxint):
    if t is None:
        return dm
        
    l = t.left
    rt = t.root
    r = t.right
    
    dm = _min(dm,rt,x)
    
    if rt == x:
        return rt
    if rt < x:
        return find(r,x,dm)
    return find(l,x,dm)
    
    
if __name__ == "__main__":
    
    t = Tree(5,
            Tree(3,
                Tree(2),
                Tree(4)),
            Tree(7,
                Tree(6),
                Tree(8)))
    
    t2 = Tree(32,
                Tree(24,
                    Tree(21,
                        Tree(14)),
                    Tree(28,
                        Tree(25),
                        Tree(31))),
                Tree(41,
                    Tree(36,
                        None,
                        Tree(39)),
                    Tree(47)))
    
    print_t(t)
    print find(t,6.7)
    # >> 7
    
    print_t(t2)
    print find(t2,29)
    # >> 28