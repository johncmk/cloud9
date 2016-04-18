class Tree:

    __slots__ = "root,left,right".split()

    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

def print_t(t,tab=1):
    if t is None:
        return
    print "\t"*tab,t.root
    print_t(t.left,tab+1)
    print_t(t.right,tab+1)       

'''preorder AKA DFS 
we can do DFS traversal from root until we find a leaf node
and print the path DFS traverse visited'''

def paths_bt(t,li = []):
    if t is None:
        return
    
    if t.left is None and t.right is None:
        li.append(t.root)
        print "path : ",li
        li.pop()
        return
    
    li.append(t.root)
    paths_bt(t.left,li)
    paths_bt(t.right,li)
    li.pop()
        
'''longest path; require 2 helper function find LCA and find the level of each node'''

'''LCA'''

def _lca(t,x,path):
    if t is None:
        return False
    
    l = t.left
    rt = t.root
    r = t.right
    
    path.append(rt)

    if rt == x:
        return True
    if _lca(l,x,path):
        return True
        
    if _lca(r,x,path):
        return True
        
    path.pop()
    return False

def lca(t, n1, n2):
    if t is None:
        return []
    
    n1_path = []
    n2_path = []
    
    n1_flag = _lca(t,n1,n1_path)
    n2_flag = _lca(t,n2,n2_path)
    
    if n1_flag == False or n2_flag == False:
        print "lca not found"
        return []
        
    print "longest path"
    print "n1_path : ",n1_path
    print "n2_path : ",n2_path
    
    length = max(n1_path , n2_path)
    i = 0
    while i < length:
        if n1_path[i] != n2_path[i]:
            break;
        i+=1
        
    return n1_path[i-1]    
    
'''level of nodes'''

def get_level(t,d,lv = 0):
    if t is None:
        return
    
    l = t.left
    rt = t.root
    r = t.right
    
    d[lv] = rt
    get_level(l,d,lv+1)
    get_level(r,d,lv+1)
    return d

import sys    
    
def getMax_level(t, d = {}):
    if t is None:
        return -1
        
    l = t.left
    rt = t.root
    r = t.right
    
    l_d = {}
    r_d = {}
    
    l_d = get_level(l,l_d)
    r_d = get_level(r,r_d)
    
    print "dictioanry left : ", l_d
    print "dictioanry right : ", r_d
    l_max_key = max(l_d)
    l_node = l_d[l_max_key]
    
    r_max_key = max(r_d)
    r_node = r_d[r_max_key]
    
    print "longest path from left ", r_node
    print "longest path from right ", r_node
    lca(t,l_node,r_node)
    
    

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
    paths_bt(t)
    
    #print "lca : ",lca(t,5,8)
    #print "level of tree : ", get_level(t)
    
    getMax_level(t)
    