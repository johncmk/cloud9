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

'''Find lca and the path of left subtree
and the right subtree.'''
def find_lca(t, n1, n2,n1_path=[],n2_path=[]):
    if t is None:
        return []
    
    n1_flag = _lca(t,n1,n1_path)
    n2_flag = _lca(t,n2,n2_path)
    
    if n1_flag == False or n2_flag == False:
        print "lca not found"
        return []
 
    length = max(n1_path , n2_path)
    i = 0
    while i < length:
        if n1_path[i] != n2_path[i]:
            break;
        i+=1
        
    return n1_path[i-1]    
    
'''level of nodes'''

def get_all_level(t,d,lv = 0):
    if t is None:
        return
    
    l = t.left
    rt = t.root
    r = t.right
    
    d[lv] = rt
    get_all_level(l,d,lv+1)
    get_all_level(r,d,lv+1)
    return d

def getMax_level(t, d = {}):
    if t is None:
        return -1
        
    l = t.left
    rt = t.root
    r = t.right
    
    l_d = {}
    r_d = {}
    
    l_d = get_all_level(l,l_d)
    r_d = get_all_level(r,r_d)
    
    l_max_key = max(l_d)
    l_node = l_d[l_max_key]
    
    r_max_key = max(r_d)
    r_node = r_d[r_max_key]
    
    lca = find_lca(t,l_node,r_node)
    
'''shortest path between two nodes'''
def shortest_path(t,n1,n2):
    if t is None:
        return
    
    n1_path = []
    n2_path = []
    
    lca = find_lca(t,n1,n2,n1_path,n2_path)
   
    for el in reversed(n1_path):
        if el == lca:
            print lca," ",
            break;
        else:
            print el," ",
            
    for el in n2_path:
        if el == lca:
            continue
        else:
            print el," ",

'''The diameter of a tree is the number of
nodes on the longest path 
between any two leaves in hte tree'''
def diameter_t(t):
    return

'''Find the only lca of two nodes'''
def find_lca2(t,n1,n2):
    if t is None:
        return t
    
    if t.root == n1 or t.root == n2:
        return t.root
    
    l_root = find_lca2(t.left,n1,n2)
    r_root = find_lca2(t.right,n1,n2)
    
    if l_root is not None and r_root is not None:
        return t.root
    
    if l_root is not None:
        return l_root
    else:
        return r_root

'''longest path aka height of the tree
the given tree will return 4 because
>[1->2->4->7] or [1->3->6->8]'''
def max_depth(t):
    if t is None:
        return 0
        
    l_lv = max_depth(t.left)
    r_lv = max_depth(t.right)
    
    return max(l_lv, r_lv)+1

'''get level of given node of the tree'''
def get_level(t,x,lv = 0):
    if t is None:
        return 0 #either tree is empty or node was never found
        
    l = t.left
    rt = t.root
    r = t.right
        
    if rt == x:
        return lv
    
    l_lv = get_level(l,x,lv+1)
    r_lv = 0
    if l_lv == 0:
        r_lv = get_level(r,x,lv+1)
        return r_lv
    else:
        return l_lv

'''Find the distance between two nodes
ex: 5->8 is 3
plan is to get LCA of the two nodes 
then find the distance'''

def dist(t,n1,n2):
    if t is None:
        return 0
    
    lca = find_lca2(t,n1,n2)
    
    left = get_level(t,n1)
    right = get_level(t,n2)
    lca_dist = 2* get_level(t,lca)
    
    print "left : ",left
    print "right : ",right
    print "lca : ", lca_dist
    return left + right - lca_dist 
    
'''Largest Sum Path'''    

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
    paths_bt(t) #print all path 
    
    print "max depth : ",max_depth(t) #print longest path from root to leaf
    
    getMax_level(t)
    shortest_path(t,4,5)
    
    print ""
    x = 3
    print "get level ",x,"  : ",get_level(t,x)
    
    print "diameater from 5 to 8 : ", dist(t,5,8)