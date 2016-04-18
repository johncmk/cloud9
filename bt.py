class Tree:

    __slots__ = "root,left,right".split()

    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right
       

'''preorder AKA DFS 
we can do DFS traversal from root until we find a leaf node
and print the path DFS traverse visited'''

def foo(t, path, pathlen):
    if t is not None:
        path[pathlen] = t.root
        pathlen+=1
        return
        
    #if node is a leaf node
    if t.left is None and t.right is None: 
        print path
        return
    else:
        foo(t.left,path,pathlen)
        foo(t.right,path,pathlen)
        
def foo2(t, sb):
    if not t:
        print(''.join(sb))
        return
    sb.append(str(t.root)+" ")
    foo2(t.left,sb)
    if t.right:
        foo2(t.right,sb)
    sb.pop()
    
def foo3(t,li,ptr):
    
    if t is None:
        return
    
    li.insert(ptr,t.root)
    ptr+=1
    
    if t.left is None and t.right is None:
        for i in range(ptr-1):
            print li[i]
        return
    
    foo3(t.left,li,ptr+1)
    foo3(t.right,li,ptr+1)
   
   
    
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
    
    #foo(t,{},0)
    #foo2(t,[])
    foo3(t,[],0)