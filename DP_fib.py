'''top-down'''        
def fib(n, memo = {0:0,1:1}):
    if n <= 1:
        return memo[n]
    if n not in memo:
        memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]

'''bottom up'''
def fib_bu(n):
    ans = [0,1]
    for i in range(2,n+1):
        ans.append(ans[i-1] + ans[i-2])
    return ans[n]
    
if __name__ == "__main__":
    
    print "top-down memoizaed DP",fib(31)
    print "bottom up DP", fib_bu(31)