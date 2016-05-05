'''
Find the number of inversion

ex [3,1,4,2]
    1) 3,1
    2) 3,2
    3) 4,3
    therefore the function returns 3 in the given case

the largest possible number of inversion can be found 
in the followin formular

n(n-1) / 2

i.e. [6,5,4,3,2,1] has n = 6

6(6-1) / 2  ->  6(5)/2  ->  30/2  -> 15 is the largest possible number of inversion.
'''
    
    
'''this is naive solution
For each element, count number of elements 
which are on right side of it and are smaller than it.
This bring solution however it's O(n)..'''    
def inversions_naive(li):
    
    if len(li) <= 1:
        return 0
    
    inv = 0    

    for i in range(len(li)):
        for j in range(i):
            if li[i] < li[j]:
                inv+=1
    return inv

'''
Optimal Solution will be using the mergesort
such that each time you merge and find the left el is greater than
the right array then increment the inverion count. O(nlogn)
'''

# inversion = inv1 + inv2 + cross_inv

def inversions(li,inv = 0):
    
    if len(li) <= 1:
        return li,inv
        
    mid = len(li)/2
    l = li[:mid]
    r = li[mid:]
    
    l,inv1 = inversions(l,inv)
    r,inv2 = inversions(r,inv)
    
    return merge(l,r,inv1+inv2)
    
def merge(l,r,inv):
    
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
            inv+=len(l)-l_pt
            m.append(r[r_pt])
            r_pt+=1
            
    return m,inv


if __name__ == "__main__":
    
    li = [3,1,4,2]
    # >> 3
    li2 = [2,4,1,3,5]
    # >> 3
    li3 = [1,20,6,4,5]
    # >> 5
    li4 = [6,5,4,3,2,1]
    # >> 15 
    
    print inversions(li)
    print inversions(li2)
    print inversions(li3)
    print inversions(li4)
