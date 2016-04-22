class Tree():

    __slots__ = "root,left,right".split()

    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

'''preorder'''
def print_t(t,tab=1):
    if t is None:
        return
    l = t.left
    rt = t.root
    r = t.right
    print '\t'*tab, rt
    print_t(l,tab+1)
    print_t(r,tab+1)

'''inorder'''
def _sorted(t,li):
    if t is None:
        return li
    l = t.left
    rt = t.root
    r = t.right
    _sorted(l,li)
    li.append(rt)
    _sorted(r,li)
    return li

def post_order(t):
    if t is None:
        return t
    l = t.left
    rt = t.root
    r = t.right
    post_order(l)
    post_order(r)
    print rt

def _search(t,x,parent=None):
    if t is None:
        return parent
    l = t.left
    rt = t.root
    r = t.right
    if rt == x:
        return t
    parent = t
    if rt < x:
        return _search(r,x,parent)
    return _search(l,x,parent)

def search(t,x):
    sub_t = _search(t,x)
    if sub_t.root != x:
        return False
    return True

def insert(t,x):
    sub_t = _search(t,x)
    if sub_t.root == x:
        print x, " already exists in BST"
        return
    #sub_t is the parent of the value x
    if sub_t.root < x:
        sub_t.right = Tree(x)
    else:
        sub_t.left = Tree(x)

#ONLY use for deletion; return parent, child
def _search_parent(t,x,parent=None):
    if t is None:
        return None,None
    l = t.left
    rt = t.root
    r = t.right
    if rt == x and parent is None:
        print x," is the root of the BST"
        return parent,t
    if rt == x:
        return parent,t
    parent = t
    if rt < x:
        return _search_parent(r,x,parent)
    return _search_parent(l,x,parent)

def _delete(parent,sub_t,rt):
    if parent.root < rt:
        parent.right = sub_t
    else:
        parent.left = sub_t
		
'''4 cases: 1) both left and right child exist
			2) ONLY right child exists
			3) ONLY left child exists
			4) both left and right child not exist'''
def delete(t,x):
    parent,t = _search_parent(t,x)

    if t is None and parent is None:
        print x," not exists in BST"
        return

    l = t.left
    rt = t.root
    r = t.right

    if l is not None and r is not None:
        key = min(_sorted(r,[])) #Return SUCCESSOR
        delete(t,key)
        t.root = key
    elif r is not None:
        _delete(parent,r,rt)
    elif l is not None:
        _delete(parent,l,rt)
    else:
        _delete(parent,None,rt)

if __name__ == "__main__":

    t = Tree(4,
                Tree(2,
                     Tree(1),
                     Tree(3)),
                Tree(6,
                     Tree(5),
                     Tree(7,
                          None,
                          Tree(9)
                          )))
    
    insert(t,11)
    insert(t,0)
    insert(t,8)
    print_t(t)
    
    print_t(t)
    insert(t,0)
    print_t(t)
    delete(t,9)
    delete(t,0)
    delete(t,6)
    

    insert(t,15)
    print_t(t)
    
    print _sorted(t,[])
    print "111 exists? ",search(t,111)
    
    insert(t,10)
    insert(t,8)
    insert(t,12)
    insert(t,18)
    print_t(t)
    print _sorted(t,[])
       
    print "15 exists? ",search(t,15)
    print _sorted(t,[])
    
    delete(t,6)
    delete(t,18)
    delete(t,8)
    delete(t,10)
    print_t(t)
    print _sorted(t,[])
    
    insert(t,11)
    print_t(t)
    print "11 exists? ", search(t,11)
    insert(t,10)
    insert(t,0)
    print_t(t)
    print _sorted(t,[])
    delete(t,10)
    delete(t,0)
    delete(t,6)
    print_t(t)
    print _sorted(t,[])
    
    post_order(t)