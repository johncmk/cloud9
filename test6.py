'''
Depth First Search

g; graph
c; color
t; time
timer; global variable that tracks the node timer
'''

dfs_timer = 0

def init_dfs(g,c,d_t,f_t):
    
    for el in g:
        c[el] = 'w' 
        d_t[el] = 0
        f_t[el] = 0

def dfs(u,g,c,d_t,f_t):
    
    global dfs_timer
    
    c[u] = "g"
    dfs_timer+=1
    d_t[u] = dfs_timer
    
    if u not in g:
        c[u] = "b"
        return
    
    for v in g[u]:
        if c[v] == "w":
            print u," -> ",v
            dfs(v,g,c,d_t,f_t)
        elif c[v] == "g":
            print u," -> ",v,"[BACK]"
        elif d_t[v] > d_t[u]:
            print u," -> ",v,"[FORWARD]"
        else:
            print u," -> ",v,"[CROSS]"
    
    dfs_timer+=1
    f_t[u] = dfs_timer
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
   
topo_timer = 0
   
# set the number of indegree egdes of each node    
def init_topo_dfs(g,c,d_t,f_t,in_degree):
    
    for el in g:
        in_degree[el] = 0
        c[el] = 'w'
        d_t[el] = 0
        f_t[el] = 0
        
    for u in g:
        for v in g[u]:
            in_degree[v] += 1

def topo_dfs(u,g,c,d_t,f_t,in_degree,stk):
    
    c[u] = 'g'
    global topo_timer
    topo_timer+=1
    d_t[u] = topo_timer
    
    if u not in g:
        c[u] = 'b'
        d_t[u] = -1
        f_t[u] = -1
        in_degree[u] = -1
    
    for v in g[u]:
        in_degree[v]-=1
        if c[v] == 'w' and in_degree[u] == 0:
            topo_dfs(v,g,c,d_t,f_t,in_degree,stk)
        elif c[v] == 'g':
            print "Cycle has detected, No Topological Order"
            return
        
    
    stk.insert(0,u)
    c[u] = 'b'
    topo_timer+=1
    f_t[u] = topo_timer
    return

if __name__ == "__main__":
    
    '''
    Shared variables
    '''
    
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
                "CS12": ["CS30"], 
                "CS20": ["CS30"],
                "CS21": ["CS20", "CS12"],
                "CS30": []
                }
    
    #color
    c = {}
    
    #time
    d_t = {} # discover time
    f_t = {} # finish time
    
    '''DFS'''
    print "====DFS===="
    
    init_dfs(g,c,d_t,f_t)
    dfs("A",g,c,d_t,f_t)
    
    '''BFS'''
    
    print "\n====BFS===="
    
    #level
    lv = {}
    
    init_bfs(g,lv)
    bfs("A",g,lv)
    
    '''Detect cycle in graph'''
    
    print "\n====DECTECT CYCLE===="
    
    is_cycle = [False] # element in the list varies over function calls because it's passing by copy address
    pi = {} #parent is required for backtracking to parent node when print the cycle path
    init_cycle_dfs(g,c)
    cycle_dfs("A",g,c,pi,is_cycle)
    
    if is_cycle[0] == False:
        print "ACYCLIC"
        
    '''Topological Sort'''
    
    print "\n====Topological Sort===="
    
    in_degree = {}
    stk = []
    
    init_topo_dfs(g_topo,c,d_t,f_t,in_degree)
    topo_dfs("CS10",g_topo,c,d_t,f_t,in_degree,stk)
    
    print "discover time : ",d_t
    print "\nfinish time : ",f_t
    
    
    while stk != []:
        if len(stk) == 1:
            print stk.pop(0)
        else:
            print stk.pop(0), " -> ",
