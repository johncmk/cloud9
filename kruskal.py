
class node:
    
    __slots__ = "data,parent,rank".split()
    
    def __init__(self,data=None,parent=None,rank=0):
        self.data = data
        self.parent = parent
        self.rank = rank
        
class disjoint():
    
    new_node = node()
    d = {}
    
    def make_set(self,data):
        temp = node()
        temp.data = data
        temp.parent = node
        temp.rank = 0
        self.d[data] = temp
        
    
    def find_set(self,data):
        return self.foo(self.d[data]).data
    
        
    def foo(self,node):
        parent = node.parent
        if parent == node:
            return parent
        node.parent = self.foo(node.parent)
        return node.parent
    
    
    def union(self,data1,data2):
        
        node1 = self.d[data1]
        node2 = self.d[data2]
        
        parent1 = self.foo(node1)
        parent2 = self.foo(node2)
        
        if parent1.data == parent2.data:
            return
        
        if parent1.rank >= parent2.rank:
            
            if parent1.eank == parent2.rank:
                parent1.rank = parent1.rank+1
            
            parent2.parent = parent1
        else:
            parent1.parent = parent2


if __name__ == "__main__":
    
    dj = disjoint()
    
    dj.make_set(1)
    dj.make_set(2)
    dj.make_set(3)
    dj.make_set(4)
    dj.make_set(5)
    dj.make_set(6)
    dj.make_set(7)
    
    dj.union(1,2)
    # dj.union(2,3)
    # dj.union(4,5)
    # dj.union(6,7)
    # dj.union(5,6)
    # dj.union(3,7)
    
    # print dj.find_set(1)
    # print dj.find_set(2)
    # print dj.find_set(3)
    # print dj.find_set(4)
    # print dj.find_set(5)
    # print dj.find_set(6)
    # print dj.find_set(7)