import heapq


'''find median in running stream'''

def get_median(min_h,max_h):
    
    heapq.heapify(min_h)
    heapq._heapify_max(max_h)
    
    if len(min_h) == len(max_h):
        temp = (min_h[0]+max_h[0])/2.0
    elif len(min_h) - len(max_h) == 1:
        temp = min_h[0]
    elif len(max_h) - len(min_h) == 1:
        temp = max_h[0]
    else:
        if len(max_h) > len(min_h):
            heapq.heappush(min_h,heapq.heappop(max_h))
        else:
            heapq.heappush(max_h,heapq.heappop(min_h))
        return get_median(min_h,max_h)
    return temp
    
def medians(li):
    
    if len(li) <= 1:
        return li
    
    max_h = []
    min_h = []
    mids = []
    
    for i in range(len(li)):
        el = li[i]
        if i == 0:
            heapq.heappush(max_h,el)
            temp = el
        else:
            
            el_mids = mids[len(mids)-1]
            
            if el <= el_mids:
                heapq.heappush(max_h,el)
            else:
                heapq.heappush(min_h,el)

            temp = get_median(min_h,max_h)

        mids.append(temp)
    
    return mids

'''find the cloest node from the BST with given x'''

class Tree:
    
    __slots__ = "root,left,right".split()
    
    def __init__(self,root = None, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right

def print_t(t,tab=1):
    if t is None:
        return
    print '\t'*tab,t.root
    print_t(t.left,tab+1)
    print_t(t.right,tab+1)

def _min(t,x,temp):
    n1 = abs(temp-x)
    n2 = abs(t.root-x)
    if n1 < n2:
        return temp
    return t.root
    
'''preorder'''
def find(t,x,temp = 0):
    if t is None:
        return temp
    
    if t.root == x:
        return t.root
        
    temp = _min(t,x,temp)
    
    if t.root < x:
        return find(t.right,x,temp)
    return find(t.left,x,temp)

'''
Find the number of inversions: Hint(MergeSort); O(NlogN)
'''

def mergeSort(li,inv = 0):
    
    if len(li) <= 1:
        return li,inv
        
    mid = len(li)/2
    
    l = li[:mid]
    r = li[mid:]
    
    l,inv1 = mergeSort(l,inv)
    r,inv2 = mergeSort(r,inv)

    return merge(l,r,inv1+inv2)


def merge(l,r,inv):
    
    total_len = len(l) + len(r)
    l_pt = 0
    r_pt = 0
    m = []
    
    while len(m) < total_len:
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
            inv+=len(l)-l_pt
            m.append(r[r_pt])
            r_pt+=1
    return m,inv


'''Given inoder and preorder traverse arrays find postorder traversal'''

def search(in_li,root,n):
    
    for i in range(n):
        el = in_li[i]
        if el == root:
            return i
    return -1

def postorder(in_li, pre_li,n):
    
    root_ads = search(in_li,pre_li[0],n)
    
    if root_ads != 0:
        postorder(in_li,pre_li[1:],root_ads)

    if root_ads < n-1:
        postorder(in_li[root_ads+1:], pre_li[root_ads+1:],n-root_ads-1)

    print pre_li[0]," ",
    
if __name__ == "__main__":
    
    '''Testing Medians'''
    
    li = [5,3,4,1,6]
    
    print medians(li)
    # >> [5,4,4,3.5,4]
    
    
    '''Tesing find closest x in BST'''
    
    t = Tree(5,
            Tree(3,
                Tree(2),
                Tree(4)),
            Tree(7,
                Tree(6),
                Tree(8)))
    
    print_t(t)
    print find(t,6.7)
    # >> 7
    
    t2 = Tree(32,
                Tree(24,
                    Tree(21,
                        Tree(14)),
                    Tree(28,
                        Tree(25),
                        Tree(31))),
                Tree(41,
                    Tree(36,
                        None,
                        Tree(39)),
                    Tree(47)))
    
    print_t(t2)
    print find(t2,29)
    # >> 28
    
    '''Testing number of inversions'''
    
    li_inv = [3,1,4,2]
    # >> 3
    li2_inv = [2,4,1,3,5]
    # >> 3
    li3_inv = [1,20,6,4,5]
    # >> 5
    li4_inv = [6,5,4,3,2,1]
    # >> 15 
    
    print "inversions : ", mergeSort(li_inv)
    print "inversions : ", mergeSort(li2_inv)
    print "inversions : ", mergeSort(li3_inv)
    print "inversions : ", mergeSort(li4_inv)
    
    
    '''Testing given inorder and preoder print postorder'''
    
    in_li = [1,2,3,5]
    pre_li = [2,1,3,5]
    
    postorder(in_li,pre_li,len(in_li))
    # >> [2,5,3,1]
    
    print "\n"    
    
    pre_li2 = [1,2,4,5,3,6]
    in_li2 = [4,2,5,1,3,6]
    
    postorder(in_li2,pre_li2,len(in_li2))
    # >> [4,5,2,6,3,1]
    
    
    