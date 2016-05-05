'''
static functions
'''
def less_than(x,y):
    return x[0]+x[1] < y[0]+y[1] or x[0]+x[1] == y[0]+y[1] and x[1] < y[1]

def _enumerate(a,b):
    li = []
    for el_a in a:
        for el_b in b:
           li.append((el_a,el_b))
    return li
    
def shuffle_li(li):
    if len(li) <= 1:
        print "nothing to shuffle"

    for i in range(len(li)-1,-1,-1):
        ptr = random.randrange(i+1)
        li[i],li[ptr] = li[ptr],li[i]
    return li

# nbesta; sort and take the top n; slowest

import random

def nbesta(a,b):
    
    li = _enumerate(a,b)
    li = qsort(li)
    return li[:4]

def qsort(li):
    if len(li) <= 1:
        return li
    
    p_adr = random.randrange(len(li))
    p = li[p_adr]
    l,eq,r = [],[],[]
    
    for i in range(len(li)):
        if i == p_adr:
            continue
        else:
            el = li[i]
            if less_than(el,p):
                l.append(el)
            elif not less_than(el,p):
                r.append(el)
            else:
                eq.append(el)
                
    return qsort(l) + eq + [p] + qsort(r)

# nbestb; qselect; slow

def nbestb(a,b):
    
    li = _enumerate(a,b)
    return qselect(li,4)
    
def qselect(li,k):
    
    if len(li) <= 1:
        return li
    
    p_adr = random.randrange(len(li))
    p = li[p_adr]
    l,eq,r = [],[],[]
    
    for i in range(len(li)):
        if i == p_adr:
            continue
        else:
            el = li[i]
            if less_than(el,p):
                l.append(el)
            elif not less_than(el,p):
                r.append(el)
            else:
                eq.append(el)
            
    if len(l) + len(eq) + 1 == k:
        return l+eq+[p]
    elif len(l) + len(eq) >= k:
        return qselect(l+eq,k)
    k = k - (len(l) + len(eq) + 1)
    return l+eq+[p]+qselect(r,k)
    
# nbestc; Dijkstra-style best-first; fast

'''
solution 1)

formula:

heapq.heappush( ( (x[0]+x[1]*10)+x[1]), (x) )

push list a into min heap (logn)
push list b into min heap (logn)

while a and b not empty
pop the minimum el from the each tree
and push it into temp heap tree with given formula
after it's done iterating through the a and b 
simply pop the first 4 el from the temp heap tree.


(1,2) = (32, (1,2))
(1,3) = (43, (1,3))
(3,2) = (52, (3,2))
(1,4) = (54, (1,4))

solution 2)

using mergesort,Dijkstra Best-Search and cube pruning, priority queue (heapq)


'''

import heapq

def nbestc(a,b):
    if len(a) == 0 or len(b) == 0:
        return 0
        
    li = []
    li2 = []
    heapq.heapify(a)
    heapq.heapify(b)
        
    while a != []:
        li.append(heapq.heappop(a))
    while b != []:
        li2.append(heapq.heappop(b))
    
    return _nbestc(li,li2,[0,0],[0,0],[(li[0],li2[0])])

def _nbestc(a,b, aptr, bptr, li = []):
    if len(li) == len(a): # you can use any number of n size of a or b
        return li
    for _ in range(len(a)):
        atmp = (a[aptr[0]],b[aptr[1]+1])
        btmp = (a[bptr[0]+1],b[bptr[0]])
        if less_than(atmp,btmp):
            li.append(atmp)
            aptr[1]+=1
            return _nbestc(a,b,aptr,bptr,li)
        elif less_than(btmp,atmp):
            li.append(btmp)
            bptr[0]+=1
            return _nbestc(a,b,aptr,bptr,li)
           
        
# Find the k smallest number in datastream

import sys

def datastream():
    k = 0
    k_flag = True
    stream = True
    
    min_h = []
    max_h = []
    
    while stream:
        
        if k_flag:
            k = int(raw_input("Please Enter integer value for k: "))
            print "You have input k = ",k
            print "To exit the datastream input 'x'."
            print "To print k smallest from list input 'print'"
            k_flag = False
        else:
            el = raw_input("input any integer: ")
            
            if el == 'print':
                if len(min_h)+len(max_h) < k:
                    print "The total number of elements are less than k = ",k
                    continue
                else:
                    break
            
            if el == 'x':
                print "Goodbye."
                break;
            
            el = int(el)
        
            if max_h == []:
                heapq.heappush(max_h,el)
            else:
                heapq._heapify_max(max_h)
                el_mx = heapq.heappop(max_h)
            
                if el > el_mx:
                    heapq.heappush(min_h,el_mx)
                    heapq.heappush(max_h,el)
                else:
                    heapq.heappush(min_h,el)
            
        heapq.heapify(min_h)
        heapq._heapify_max(max_h)


# k-way mergesort
def mergeSort(li,k):
    if len(li) <= 1:
        return li
    if len(li) < k:
        print "Enter k that is greater than the list length."
        return k
    k_mid = len(li)/k
    l = li[:k_mid]
    md = li[k_mid:k_mid*2]
    r = li[k_mid*2:]
    heapq.heapify(l)
    heapq.heapify(md)
    heapq.heapify(r)
    return merge(l,md,r)
    
def merge(l,md,r):
    
    temp = []
    m = []
    len_l = len(l)
    len_md = len(md)
    len_r = len(r)
    
    # these are sentinel to find which heap tree did the element popped from.
    min_el = 0
    d = {'l':0, 'md':0, 'r':0}
    
    while len(m) < len_l + len_md + len_r:

        if l != [] and d['l'] == min_el:
            l_el = heapq.heappop(l)
            heapq.heappush(temp,l_el)
            d['l'] = l_el
        if md != [] and d['md'] == min_el:
            md_el = heapq.heappop(md)
            heapq.heappush(temp,md_el)
            d['md'] = md_el
        if r != [] and d['r'] == min_el:
            r_el = heapq.heappop(r)
            heapq.heappush(temp,r_el)
            d['r'] = r_el
            
        heapq.heapify(temp)
        min_el = heapq.heappop(temp)
        m.append(min_el)
  
    return m


if __name__ == "__main__":
    
    a = [4,1,5,3]
    b = [2,6,3,4]
    
           
    # print "nbesta : ",nbesta(a,b)
    # print "nbestb : ",nbestb(a,b)
    # print "nbestc : ",nbestc(a,b)
    
    #datastream()
    
    # li = [4,1,5,2,6,3,7,0]
    
    li = shuffle_li(range(1000000))
    
    # print qsort2(li)
    # g =  qsort2(li)
    # print len(g)

    print mergeSort(li,15)    
    # f =  mergeSort(li)
    # print len(f)