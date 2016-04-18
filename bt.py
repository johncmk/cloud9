class Tree():

    __slots__ = "root,left,right".split()

    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right
        
if __name__ == "__main__":
    
    print 5