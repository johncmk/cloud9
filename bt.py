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
    if _lca(l,x,path) or _lca(r,x,path):
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
        

'''Find the only lca of two nodes'''
def get_lca(t,n1,n2):
    if t is None:
        return t #eventually return None
    if t.root == n2:
        return t.root
    if t.root == n1:
        return t.root
    l_root = get_lca(t.left,n1,n2)
    r_root = get_lca(t.right,n1,n2)
    if l_root is not None and r_root is not None:
        return t.root
    elif l_root is not None:
        return l_root
    else: 
        return r_root

'''Get Maximum depth from root to leaf; count the number of the edges'''
def max_depth(t):
    if t is None:
        return -1
    l_dth = max_depth(t.left)
    r_dth = max_depth(t.right)
    return max(l_dth,r_dth)+1

'''Longest path aka height of the tree
the given tree will return 4 because
>[1->2->4->7] or [1->3->6->8]
count the nunber of the nodes'''
def get_height(t):
    if t is None:
        return 0
    l_lv = get_height(t.left)
    r_lv = get_height(t.right)
    return max(l_lv, r_lv)+1

'''Nodes: get level of given node of the tree; level = depth + 1'''
def get_level(t,x,level = 1):
    if t is None:
        return 0 #either tree is empty or node was never found
    if t.root == x:
        return level
    l_lv = get_level(t.left,x,level+1)
    if l_lv != 0:
        return l_lv
    r_lv = get_level(t.right,x,level+1)
    return r_lv

'''Edges: get depth of given node of the tree'''
def get_depth(t,x,depth=0):
    if t is None:
        return 0 #either tree is empty or node was never found
    if t.root == x:
        return depth
    l_dth = get_depth(t.left,x,depth+1)
    if l_dth != 0:
        return l_dth
    r_dth = get_depth(t.right,x,depth+1)
    return r_dth
    

'''Find the distance between two nodes
ex: 5->8 is 3; count the edges in distance
plan is to get LCA of the two nodes 
then find the distance 
left + right - 2 * lca can be equivalent to
(left-lca) + (right-lca). it's alternative.'''
def distance(t,n1,n2):
    if t is None:
        return 0
    lca = get_lca(t,n1,n2)
    left = get_depth(t,n1)
    right = get_depth(t,n2)
    lca_dist = 2 * get_depth(t,lca)
    return left + right - lca_dist 
    
'''Largest Sum Path'''    
def largest_sum(t):
    if t is None:
        return 0
    
    if t.left is None and t.right is None:
        return t.root
        
    l = t.left
    rt = t.root
    r = t.right
        
    l_v = largest_sum(l) + rt #path2
    r_v = largest_sum(r) + rt #path3
    
    all_v = l_v + r_v #path1
    return max(l_v,r_v,all_v)
 
'''Breath First Traverse'''   
def bfs(t):
    if t is None:
        return
    q = []
    q.insert(0,t)
    while q != []:
        t = q.pop(0)
        print t.root
        if t.left is not None:
            q.append(t.left)
        if t.right is not None:
            q.append(t.right)
            
'''The diameter of a tree is the number of
nodes on the longest path 
between any two leaves in the tree
max(l_dm, r_dem) is the node path without the root
l_ht + r_ht + 1 is the node path with the root'''
def diameter(t):
    if t is None:
        return 0
    l_ht = get_height(t.left)
    r_ht = get_height(t.right)
    l_dm = diameter(t.left)
    r_dm = diameter(t.right)
    return max( max( l_dm,r_dm ),l_ht+r_ht+1 )
    
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
    
    print "======Tree Diagream======"
    print_t(t)
    print "========================="
    
    print "======All Paths======"
    paths_bt(t) #print all path
    print "====================="
    
    print "====LCA, Depth, Level, Distance, Height of Tree, Diameter===="
    print "get only lca : ", get_lca(t,5,8)
    print "get only depth of node : ", get_depth(t,4)
    print "get only level of node : ", get_level(t,6)
    print "distance from 5 to 8 : ", distance(t,5,8)
    print "get height of the tree : ", get_height(t) #print longest path from root to leaf
    print "diameter : ", diameter(t)
    print "============================================================="
    print "========BFS========"
    bfs(t)
    print "==================="
    print "==================="
    print "max depth : ", max_depth(t)
    
    '''
    print_t(t)
    
    
    getMax_level(t)
    shortest_path(t,4,5)
    
    print ""
    x = 3
    print "get level ",x,"  : ",get_level(t,x)
    
    print "diameater from 5 to 8 : ", dist(t,5,8)
    
    print "largest_sum : ",largest_sum(t)
    '''