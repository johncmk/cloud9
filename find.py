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

def find(t,x, d={}):
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
        return find(t.left,x,d)
    if x > rt:
        return find(t.right,x,d)

if __name__ == "__main__":
    
    t = Tree(5,
            Tree(3,
                Tree(2),
                Tree(4)),
            Tree(7,
                Tree(6),
                Tree(8)))
    
    print_t(t)
    
    print find(t,6.7)