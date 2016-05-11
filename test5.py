
'''
Maximum weighted independent Set on a Path Graph
'''

def max_wis(li):
    
    if len(li) <= 1:
        return li
        
    if li[0] < 0:
        incl = 0
    else:
        incl = li[0]
    excl = 0
    
    ret = 0
    
    for i in range(1,len(li)):
        
        sub_set1 = excl + li[i]
        sub_set2 = incl
        excl_next = incl
        incl = max(sub_set1,sub_set2)
        excl = excl_next
        
    return incl
    
'''
Number of BSTs in given n-nods
'''    
    
def bsts(n):
    
    if n <= 1:
        return 1
        
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2,n+1):
        for j in range(1,i+1):
            dp[i] = dp[i] + (dp[j-1] * dp[i-j])
            
    return dp[n]
    
    
    
if __name__ == "__main__":
    
    print max_wis([7,8,5])
    # >> 12
    
    print max_wis([-1,8,10])
    # >> 10
    
    print max_wis([])
    # >> 0
    
    print max_wis([-1,3,-5,4,6,-1,2,-7,13,-3])
    # >> 17
    
    
    
    print bsts(3)
    # >> 5
    
    print bsts(5)
    # >> 42