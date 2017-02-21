class Tree:
    
    __slot__ = "root,left,right".split()
    
    def __init__(self,root=None,left=None,right=None):
        self.root = root
        self.left = left
        self.right = right

#print tree; preorder
def print_t(t, tab=0):
    if t is None:
        return 
    print '\t'*tab,t.root
    print_t(t.left,tab+1)
    print_t(t.right,tab+1)

#print all path


if __name__ == "__main__":
    
    t = Tree(3,
            Tree(2,
                Tree(4),
                Tree(5)),
            Tree(1,
                Tree(7),
                Tree(8)))
    
    print_t(t)