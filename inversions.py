'''Find the number of inversion
ex [3,1,4,2]
    1) 3,1
    2) 3,2
    3) 4,3
    therefore the function returns 3 in the given case'''
    
    
'''this is lazy solution
For each element, count number of elements 
which are on right side of it and are smaller than it.
This bring solution however it's O(n)..'''    
def inversions_lazy(li):
    
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
the right array then increment the inverion count'''




if __name__ == "__main__":
    
    li = [3,1,4,2]
    # >> 3
    li2 = [2,4,1,3,5]
    # >> 3
    li3 = [1,20,6,4,5]
    # >> 5
    print inversions_lazy(li3)
    
    print len(li2)/2
    