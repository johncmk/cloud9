class Tree:

    __slots__ = "root,left,right".split()

    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right
       

'''preorder AKA DFS 
we can do DFS traversal from root until we find a leaf node
and print the path DFS traverse visited'''

def foo(t,li = [],lv = 0):
    if t is None:
        return
    
    if t.left is None and t.right is None:
        li.append(t.root)
        print "path : ",li
        li.pop()
        return
    
    li.append(t.root)
    foo(t.left,li,lv+1)
    foo(t.right,li,lv+1)
    li.pop()
    
def print_t(t,tab=1):
    if t is None:
        return
    print "\t"*tab,t.root
    print_t(t.left,tab+1)
    print_t(t.right,tab+1)
        
if __name__ == "__main__":
    
    t = Tree(1,
                Tree(2,
                    Tree(4,
                        None,
                        Tree(7))),
                Tree(3,
                    Tree(5),
                    Tree(6
                        ,Tree(8))))
                        
    
    print_t(t)
    foo(t)