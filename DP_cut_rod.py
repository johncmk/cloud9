'''bottom up approach'''
def cut_rod(n):
    
    if n <= 1:
        return n
    
    p = [0,1,5,8,10,13,17,18,22,25,30]
    max_rev = 0
    no_cut = p[n]
    
    for i in range(n):
        for j in range(n):
            if i + j > n:
                return max_rev
            if i + j == n:
                temp = p[i] + p[j]
                max_rev = max(no_cut, temp)
    return max_rev
    
    
if __name__ == "__main__":
    
    print "max revenue : ", cut_rod(10)