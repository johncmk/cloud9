'''Topological sort in bfs'''


'''Set level and in_degree'''
def init_bfs(graph, level, in_degree, q):

    for u in graph:
        level[u] = -1
        in_degree[u] = 0

    for u in graph:
        for v in graph[u]:
            in_degree[v]+=1

    for el in graph:
        if in_degree[el] == 0:
            q.append(el)

'''Topological Sort in BFS'''

def bfs(graph, level, q, path = []):
    while q != []:
        u = q.pop(0)
        for v in graph[u]:
            in_degree[v]-=1

            if level[v] < level[u] and in_degree[v] == 0:
                print "Back"
            
            elif level[v] == -1 and in_degree[v] == 0:
                level[v] = level[u] + 1
                q.append(v)
                path.append(v)
    return path
                


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
    q = []

    init_bfs(graph, level, in_degree, q)
    path = bfs(graph, level, q)

    print path



