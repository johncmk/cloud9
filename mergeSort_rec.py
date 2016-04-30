
def mergeSort(li):
    
    if len(li) <= 1:
        return
    _mergeSort(li,0,len(li)-1)


def _mergeSort(li,low,high):

    if low < high:
        mid = low + (high-low)/2
        _mergeSort(li,low,mid)
        _mergeSort(li,mid+1,high)
        merge(li,low,mid,high)


def merge(li,low,mid,high):
    
    n1 = mid-low+1
    n2 = high-mid
    
    # temp lists with the given size that are n1 and n2
    l = [0]*n1
    r = [0]*n2
    
    # split the list into temp arrays 
    for i in range(n1):
        l[i] = li[low+i]
    for j in range(n2):
        r[j] = li[mid+1+j]
        
    #merge the temp list back to li
    i = 0
    j = 0
    k = low

    while i < n1 and j < n2:
        
        if l[i] < r[j]:
            li[k] = l[i]
            i+=1
        else:
            li[k] = r[j]
            j+=1
        k+=1
        
    while i < n1:
        li[k] = l[i]
        i+=1
        k+=1
        
    while j < n2:
        li[k] = r[j]
        j+=1
        k+=1




if __name__ == "__main__":
    
    li = [6,1,5,2,4,3,1,1,5,10]    

    print mergeSort(li)
    print li