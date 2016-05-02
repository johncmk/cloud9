import random

'''shuffle list'''
def shuffle_li(li):
    if li <= 1:
        return li
    
    for i in range(len(li)-1,-1,-1):
        if i == 0:
            break
        rand = random.randrange(0,i)
        li[i],li[rand] = li[rand],li[i]
        
    return li


'''qsort'''
def qsort(li):
    
    if li == []:
        return li
    
    p_adr = random.randrange(len(li))
    p = li[p_adr]
    l,eq,r = [],[],[]
    
    for i in range(len(li)):
        if i == p_adr:
            continue
        else:
            el = li[i]
            if el < p:
                l.append(el)
            elif el > p:
                r.append(el)
            else:
                eq.append(el)
                
    return qsort(l) + eq + [p] + qsort(r)
    
'''msort'''
def msort(li):
    
    if len(li) <= 1:
        return li
        
    mid = len(li)/2
    l = li[:mid]
    r = li[mid:]
    l = msort(l)
    r = msort(r)
    return merge(l,r)

def merge(l,r):
    l_pt = 0
    r_pt = 0
    m = []
    
    while len(m) < len(l) + len(r):
        if l_pt == len(l):
            m.append(r[r_pt])
            r_pt+=1
        elif r_pt == len(r):
            m.append(l[l_pt])
            l_pt+=1
        elif l[l_pt] <= r[r_pt]:
            m.append(l[l_pt])
            l_pt+=1
        else:
            m.append(r[r_pt])
            r_pt+=1
            
    return m
    
'''quick select'''    
def qselect(li,k):
    if li == []:
        return li
        
    p_adr = random.randrange(len(li))
    p = li[p_adr]
    l,eq,r = [],[],[]
    
    for i in range(len(li)):
        if i == p_adr:
            continue
        else:
            el = li[i]
            if el < p:
                l.append(el)
            elif el > p:
                r.append(el)
            else:
                eq.append(el)
    
    if len(l) + len(eq) + 1 == k:
        return p
    if len(l) + len(eq) >= k:
        return qselect(l+eq,k)
    k = k - (len(l) + len(eq) + 1)
    return qselect(r,k)
    
'''bst; sort, search, insert, delete'''    

class Tree:
    
    __slots__ = "root,left,right".split()
    
    def __init__(self,root = None, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right

'''preorder'''    
def print_t(t, tab=1):
    if t is None:
        return
    print '\t'*tab, t.root
    print_t(t.left,tab+1)
    print_t(t.right,tab+1)
    
'''sorted; inorder'''    
def _sorted(t,li):
    if t is None:
        return li
    _sorted(t.left,li)
    li.append(t.root)
    _sorted(t.right,li)
    return li

'''search'''
def _search(t,x,parent=None):
    if t is None:
        return parent
    if t.root == x:
        return t
    parent = t
    if t.root < x:
        return _search(t.right,x,parent)
    return _search(t.left,x,parent)

def search(t,x):
    spot = _search(t,x)
    if spot.root != x:
        return False
    return True

'''insert'''
def insert(t,x):
    spot = _search(t,x)
    if spot.root == x:
        print x, " already exists in the tree"
    else:
        if spot.root < x:
            spot.right = Tree(x)
        else:
            spot.left = Tree(x)

'''search only used for delete; return both root and its parent'''
def search_adv(t,x,parent = None):
    if t is None:
        return parent,t 
        
    if t.root == x:
        return parent,t
    parent = t
    if t.root < x:
        return search_adv(t.right,x,parent)
    return search_adv(t.left,x,parent)


'''delete
    1) root has no child
    2) root has both child
    3) root has child at only left
    4) root has child at only right
'''
def delete(t,x):
    parent,t = search_adv(t,x)
    
    if t is None:
        print x, " not exists in BST"
        return
    
    if t.left is not None and t.right is not None:
        successor = min(_sorted(t.right,[]))
        delete(t,successor)
        t.root = successor
    elif t.left is not None:
        _delete(parent,t,t.left)
    elif t.right is not None:
        _delete(parent,t,t.right)
    else:
        _delete(parent,t,None)

def _delete(parent,t,t_branch):
    if parent.root < t.root:
        parent.right = t_branch
    else:
        parent.left = t_branch
    
if __name__ == "__main__":
    
    li = range(1,11)
    
    print "quick sort"
    print shuffle_li(li)
    print qsort(li)
    
    print "merge sort"
    print shuffle_li(li)
    print msort(li)
    
    print "quick select"
    print shuffle_li(li)
    print qselect(li,5)
    
    print "BST"
    
    t = Tree(5,
            Tree(3,
                Tree(1),
                Tree(4)),
            Tree(10,
                Tree(8),
                Tree(9,
                    None,
                    Tree(12))))
    
    
    print_t(t)
    print _sorted(t,[])
    print search(t,12)
    
    print "insert 14,7,6"
    insert(t,14)
    insert(t,7)
    insert(t,6)
    print_t(t)
    print _sorted(t,[])
    
    print "delete 14, 12, 3, 7, 5"
    delete(t,14)
    delete(t,12)
    delete(t,3)
    delete(t,7)
    delete(t,5)
    print_t(t)
    print _sorted(t,[])