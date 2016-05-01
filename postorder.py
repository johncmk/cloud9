'''
Postorder given preorder and inroder traversals
O(n) time.
'''

def search(in_li,root,n):
    for i in range(n):
        el = in_li[i]
        if el == root:
            return i
    return -1

def postorder(in_li,pre_li,n=0):
    
    root_ads = search(in_li,pre_li[0],n)

    if root_ads != 0:
        postorder(in_li, pre_li[1:],root_ads)
        
    if root_ads != n-1:
        postorder(in_li[root_ads+1:],pre_li[root_ads+1:],n-root_ads-1)
    
    print pre_li[0], " ",

if __name__ == "__main__":
    
    preli = [1,2,3,5]
    inli = [2,1,3,5]
    
    pre_li = [1,2,4,5,3,6]
    in_li = [4,2,5,1,3,6]

    postorder(inli,preli,len(preli))
    # >> [2,5,3,1]
    
    print ""
    
    postorder(in_li,pre_li,len(pre_li))
    # >> [4,5,2,6,3,1]
    