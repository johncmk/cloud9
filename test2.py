class Tree:
    
    __slots__ = "root,left,right".split()
    
    def __init__(self,root = None,left = None ,right = None):
        self.root = root
        self.left = left
        self.right = right

'''preorder'''    
def print_t(t,tab=1,sub="rt: "):
    if t is None:
        return
    print '\t'*tab,sub,t.root
    print_t(t.left,tab+1,"l: ")
    print_t(t.right,tab+1,"r: ")

def get_height(t):
    if t is None:
        return 0
    l = get_height(t.left)
    r = get_height(t.right)
    return max(l,r)+1

def bt_path(t,li=[]):
    if t is None:
        return
    if t.left is None and t.right is None:
        print li+[t.root]
        return
    li.append(t.root)
    bt_path(t.left,li)
    bt_path(t.right,li)
    li.pop()
    
def get_lca(t,n1,n2):
    if t is None:
        return t
    if t.root == n1 or t.root == n2:
        return t.root

    l_root = get_lca(t.left,n1,n2)
    r_root = get_lca(t.right,n1,n2)
    
    if l_root is not None and r_root is not None:
        return t.root #return LCA
    elif l_root is not None:
        return l_root #return node that is found in n1 or n2
    else:
        return r_root #return node that is found in n1 or n2
    
# get depth of given node
def get_depth(t,x,depth=1):
    if t is None:
        return 0 # keep returning zero until the function find the x
    if t.root == x:
        return depth # finally returnd the depth which had been cumulatively inreased
    l = get_depth(t.left,x,depth+1)
    if l != 0: 
        return l #if the x is found then l shouldn't be zero, therefore return the depth
    r = get_depth(t.right,x,depth+1)
    return r # if l is zero means the x never found in the left subtree therefore search in right subtree until the fundtion finds the x then return the depth
    
# get distance between two nodes in tree
def distance(t,n1,n2):
    if t is None:
        return t
    lca = get_lca(t,n1,n2)
    n1_d = get_depth(t,n1)
    n2_d = get_depth(t,n2)
    lca_d = get_depth(t,lca)
    return (n1_d + n2_d) - (2*lca_d)
    
# find the longest distance in tree
def longest_dist(t):
    if t is None:
        return 0
    l_h = get_height(t.left)
    r_h = get_height(t.right)
    l_ld = longest_dist(t.left)
    r_ld = longest_dist(t.right)
    return max( max(l_ld,r_ld), l_h+r_h+1)
 
# max sum
def max_sum(t):
    x = [0] # this is necessary to edit original value while in recursive
    _max_sum(t,x)
    return x[0]

def _max_sum(t,x=[0]):
    if t is None:
        return 0
    l = _max_sum(t.left,x)
    r = _max_sum(t.right,x)
    x[0] = max(x[0], l+r+t.root)
    return max(l,r)+t.root

#mirror tree
def mirror_tree(t):
    if t is None:
        return t
        
    mirror_tree(t.left)
    mirror_tree(t.right)
    
    temp = t.left
    t.left = t.right
    t.right = temp
    
# inorder
def _sorted(t,li):
    if t is None:
        return 0
    
    _sorted(t.left,li)
    li.append(t.root)
    _sorted(t.right,li)
    return li


# find kth node in BST 
def qselect_bst(t,k):
    if t is None:
        return t
    cnt = [0]
    _qselect(t,k,cnt)
    return cnt[0]
    
def _qselect(t,k,cnt):
    if t is None:
        return t
    _qselect(t.left,k,cnt)
    cnt[0]+=1
    if cnt[0] == k:
        print "t.root : ",t.root
        return
    _qselect(t.right,k,cnt) 
  
# quick select in BST   
'''
def qselect(index, t):
    if t is None:
        return 0,None
    
    l = t.left
    rt = t.root
    r = t.right
    
    num, x = qselect(index,l)
    
    if index == num + 1:
        return index,rt
    if index <= num:
        return index,x
    num2,y = qselect(index-num-1,r)
    return num+num2+1,y
'''

def qselect(k, t):
    if t is None:
        return 0,None
    
    l = t.left
    rt = t.root
    r = t.right
    
    num,x = qselect(k,l)
    
    if num + 1 == k:
        return k,rt
    if num >= k:
        return k,x
    k = k - (num+1)    
    num2,y = qselect(k,r)
    return num+num2+1,y

# find the closest number in unsorted

import random

def qselect_unsorted(li,x,k):
    if len(li) <= 1:
        return li
        
    p_adr = random.randrange(len(li))
    p = li[p_adr]
    l,eq,r = [],[],[]
    
    p_abs = abs(p-x)
    for i in range(len(li)):
        if i == p_adr:
            continue
        else:
            el = li[i]
            el_abs = abs(el-x)
            if el_abs < p_abs:
                l.append(el)
            elif el_abs > p_abs:
                r.append(el)
            else:
                eq.append(el)
                
    if len(l) + len(eq) + 1 == k:
        return l+eq+[p]
    elif len(l) + len(eq) >= k:
        return qselect_unsorted(l+eq,x,k)
    k = k - (len(l) + len(eq) - 1)
    return qselect_unsorted(r,x,k)
        
if __name__ == "__main__":
    
    
    t = Tree(1,
            Tree(2,
                Tree(4,
                    None,
                    Tree(7))),
            Tree(3,
                Tree(5),
                Tree(6,
                    Tree(8))))
                    
    print_t(t)
    print "Tree height: ",get_height(t)
    bt_path(t)
    
    print "LCA : ",get_lca(t,4,8)
    
    print get_depth(t,4)
    print "distance : ", distance(t,8,4)
    
    print "max_sum_path : ",max_sum(t)
    
    print "======Normal Tree====="
    print_t(t)
    print "======Mirror Tree====="
    mirror_tree(t)
    print_t(t)
    
    t2 = Tree(1,
                Tree(2,
                    Tree(4),
                    Tree(3)),
                Tree(5,
                    Tree(6,
                        Tree(8),
                        Tree(9,
                            None,
                            Tree(10,
                                Tree(13)))),
                    Tree(7,
                        None,
                        Tree(11,
                            None,
                            Tree(12,
                                None,
                                Tree(14))))))
     
    print "====New Binary Tre===="                           
    print_t(t2)
    
    bt_path(t2)
    
    print longest_dist(t2)
    
    
    bst = Tree(20,
                Tree(8,
                    Tree(4),
                    Tree(12,
                        Tree(10),
                        Tree(14))),
                Tree(22))
                
    print_t(bst)
    
    print "sorted : ", _sorted(bst,[])
    
    # print "kth node : ",qselect_bst(bst,4)
    
    print "kth node advanced : ", qselect(4,bst)
    
    