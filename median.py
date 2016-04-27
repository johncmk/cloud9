'''running median O(lgn)'''

'''non-data stream version, use min_heap and max_heap'''

import heapq

def _median(li,min_h,max_heap):
    
    for el in li:
        if min_h == []:
            heapq.heappush(el,min_h)
            heapq.heapify(min_h)
        

def median(li):
    if len(li) == 0:
        return li
    min_h = []
    max_h = []
    _median(li,min_h,max_h)

if __name__ == "__main__":
