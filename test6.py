'''
Depth First Search

g; graph
c; color
t; time
timer; global variable that tracks the node timer
'''

dfs_timer = 0

def init_dfs(g,c,t):
    
    for el in g:
        c[el] = 'w' 
        t[el] = 0

def dfs(u,g,c,t):
    
    global dfs_timer
    
    c[u] = "g"
    t[u] = dfs_timer
    dfs_timer+=1
    
    if u not in g:
        c[u] = "b"
        return
    
    for v in g[u]:
        if c[v] == "w":
            print u," -> ",v
            dfs(v,g,c,t)
        elif c[v] == "g":
            print u," -> ",v,"[BACK]"
        elif t[v] > t[u]:
            print u," -> ",v,"[FORWARD]"
        else:
            print u," -> ",v,"[CROSS]"

    c[u] = "b"
    return


'''
Breadth First Search

g; graph
lv; level

'''

def init_bfs(g,lv):
    
    for el in g:
        lv[el] = -1

def bfs(u,g,lv):
    
    path = []
    back = []
    cross = []
    
    lv[u] = 0
    q = [u]
    
    while q != []:
        u = q.pop(0)
        path.append(u)
        for v in g[u]:
            if lv[v] == -1:
                lv[v] = lv[u] + 1
                q.append(v)
            elif lv[u] > lv[v]:
                back.append(u+"->"+v)
            else:
                cross.append(u+"->"+v)
                
    print "PATH : ",path
    print "BACK : ",back
    print "CROSS : ",cross
    print "FORWARD : 'FORWARD NOT EXIST IN BFS TRAVERSAL'"
    
    
'''
Detect Cycle using DFS
'''    
    
def init_cycle_dfs(g,c):
    for el in g:
        c[el] = 'w'
    
def cycle_dfs(u,g,c,pi,is_cycle):
    
    c[u] = 'g'
    
    if u not in g:
        c[u] = "b"
        
    for v in g[u]:
        pi[v] = u
        if c[v] == 'w':
            cycle_dfs(v,g,c,pi,is_cycle)
        elif c[v] == 'g':
            is_cycle[0] = True
            print_cycle(pi,u,v)
            return
        
    c[u] = 'b'
    return

def print_cycle(pi,u,v):
    
    stk = [v,u] # declare stack to print cycle
    
    p = pi[v]
    while p != v:
        p = pi[p]
        stk.append(p)
    
    print "Cycle Detected : ",
    while stk != []:
        print stk.pop()," ",
        

'''
Topological Sort using DFS and BFS
'''
   
# set the number of indegree egdes of each node    
# def init_topo_dfs(g,)

if __name__ == "__main__":
    
    #graphs 
    
    g = {
        "A":["B"],
        "B":["C","D","E"],
        "C":["E"],
        "D":["A","E"],
        "E":[]
    }
    
    g_topo = {
                "CS10": ["CS20", "CS11"],
                "CS11": ["CS21"],
                "CS20": ["CS30"],
                "CS21": ["CS20", "CS12"],
                "CS12": ["CS30"],
                "CS30": []
                }
    
    #color
    c = {}
    
    #time
    t = {}
    
    
    '''DFS'''
    print "====DFS===="
    
    
    init_dfs(g,c,t)
    
    dfs("A",g,c,t)
    
    
    '''BFS'''
    
    print "\n====BFS===="
    
    
    #level
    lv = {}
    
    init_bfs(g,lv)
    bfs("A",g,lv)
    
    
    '''Detect cycle in graph'''
    
    print "\n====DECTECT CYCLE===="
    
    init_cycle_dfs(g,c)
    
    is_cycle = [False] # element in the list varies over function calls because it passing by copy address
    pi = {} #parent is required for backtracking to parent node when print the cycle path
    cycle_dfs("A",g,c,pi,is_cycle)
    
    if is_cycle[0] == False:
        print "ACYCLIC"
        
        
