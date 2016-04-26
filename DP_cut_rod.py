'''
r1 = 1 from solution 1 = 1 (no cuts) ; []
r2 = 5 from solution 2 = 2 (no cuts) ; [][]
r3 = 8 from solution 3 = 3 (no cuts) ; [][][]
r4 = 10 from solution 4 = 2 + 2 ; [][][][]   ->  [][]   [][] 
r5 = 13 from solution 5 = 2 + 3 ; [][][][][]   ->  [][]   [][][]
r6 = 17 from solution 6 = 6 (no cuts) ; [][][][][][]
r7 = 18 from solution 7 = 1 + 6 or 7 = 2 + 2 + 3 ; [][][][][][]  -> []   [][][][][][] or [][]   [][]   [][][] 
r8 = 22 from solution 8 = 2 + 6 ; [][][][][][][][]   -> [][]   [][][][][][]
r9 = 25 from solution 9 = 3 + 6 ; [][][][][][][][][]   ->   [][][]   [][][][][][]
r10 = 30 from solution 10 = 10 (no cuts) [][][][][][][][][][]
'''


'''No DP because this function does not
construct an optimal solution from computed information
it rathert solves the problem based on the p list. Therefore,
the max revenue won't be able to achieve the goal.'''
def cut_rod_test(n):
    
    if n <= 0:
        return n
    
    p = [0,1,5,8,9,10,17,17,20,24,30]
    max_rev = 0
    no_cut = p[n]
    
    for i in range(n):
        for j in range(i+1):
            if i + j > n:
                return max_rev
            if i + j == n:
                temp = p[i] + p[j]
                max_rev = max(no_cut, temp)
    return max_rev


def foo2(n):
    
    if n <= 0:
        return n
    
    p = [1,5,8,9,10,17,17,20,24,30]
    rev = [0,1]
    
    for i in range(1,n+1):
        max_val = 0
        for j in range(i):
            max_val = max( rev[i], p[j] + rev[i-j-1])
        rev.append(max_val)
    return rev[n]
   
   
def foo3(p,n):
    
    dp = [0 for i in range(n+1)]
    dp[0] = -10
    
    for i in range(1,n+1):
        for j in range(i):
            dp[i] = max(dp[i], p[j] + dp[i-j-1])
    return dp[n]
    
if __name__ == "__main__":
    
    p = [1,5,8,9,10,17,17,20,24,30]
    
    print foo2(9)
    print foo3(p,7)
    #print "max revenue : ", cut_rod_test(4)