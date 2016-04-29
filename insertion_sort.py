
'''
Insertions sort
insertions sort is useful
to sort suffled arrange card
and it is widely used for many situation 
desptite the fact that its time complexity is 
nearly O(n^2). 
this algorithm can help mergesort to acheive the better
design algorithm such that does not use extra space.
'''

def ins_sort(li):
    
    if len(li) <= 1:
        return li
    
    for i in range(1,len(li)):
        key = li[i]
        j = i-1
        
        while j >= 0 and key < li[j]:
            li[j+1] = li[j]
            j-=1
        li[j+1] = key
                
    return li

if __name__ == "__main__":
    
    li = [6,1,45,2,3,4,3,1,1,6,5,4]
    
    print ins_sort(li)