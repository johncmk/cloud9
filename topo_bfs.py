'''Topological sort in bfs'''


'''Set level and in_degree'''
def init_bfs(graph, level, in_degree):

    #set level and in_degree
    for u in graph:
        level[u] = -1
        in_degree[u] = 0

    #Give value to each in_degree
    for u in graph:
        for v in graph[u]:
            in_degree[v]+=1

'''Topological Sort in BFS'''

def bfs(u,graph, level, in_degree):
    
    level[u] = 0
    path = [u]
    q = [u]
    
    while q != []:
        u = q.pop(0)
        for v in graph[u]:
            in_degree[v]-=1

            if level[v] == -1 and in_degree[v] == 0:
                level[v] = level[u] + 1
                q.append(v)
                path.append(v)
                
            # elif level[u] > level[v]:
            #     print u,"->",v,"Back"
    
    print path
                


if __name__ == "__main__":

    graph = {
             "CS10": ["CS11", "CS20"],
             "CS11": ["CS21"],
             "CS20": ["CS30"],
             "CS21": ["CS12", "CS20"],
             "CS12": ["CS30"],
             "CS30": []
                         }

    level = {}
    in_degree = {}

    init_bfs(graph, level, in_degree)
    bfs("CS10",graph, level,in_degree)