import heapq


import random
def mid_rule(max_h,min_h,rule='a'):
    
    return {
        'a': (max_h[0] + min_h[0])/2.0,
        'b': min_h[0],
        'c': max_h[0],
        'd': random.choice([min_h[0],max_h[0]])
    }.get(rule,(max_h[0] + min_h[0])/2.0)

def get_median(max_h,min_h):
    
    heapq._heapify_max(max_h)
    heapq.heapify(min_h)
    
    if len(max_h) == len(min_h):
        temp = mid_rule(max_h,min_h,'h')
    elif len(max_h) - len(min_h) == 1:
        temp = max_h[0]
    elif len(min_h) - len(max_h) == 1:
        temp = min_h[0]
    else: #else balance the tree and recusively get temp again
        if len(max_h) - len(min_h) > 1:
            heapq.heappush(min_h,heapq.heappop(max_h))
        elif len(min_h) - len(max_h) > 1:
            heapq.heappush(max_h,heapq.heappop(min_h))
        return get_median(max_h,min_h)
    return temp
        
def medians(li):
    
    if len(li) <= 1:
        return li
    
    min_h = [] # right side
    max_h = [] # left side
    li_m = [] # collect the medians 
    
    for el in li:
        if max_h == [] and min_h == []:
            temp = el
            heapq.heappush(max_h,el)
        else:    
            mid = li_m[len(li_m)-1]
            
            if el <= mid:
                heapq.heappush(max_h,el)
            else:
                heapq.heappush(min_h,el)
                
            temp = get_median(max_h,min_h)
            
        li_m.append(temp)
        
    return li_m
    
if __name__ == "__main__":

    li = [5,3,4,1,6]
    # expected output >> [5,4,4,3.5,4]
    li2 = [5,15,1,3]
    # expected output >> [5,10,5,4]
    li3 = [12,7,8,11]
    # expected output >> [12,9.5,8,9.5]

    print medians(li)
    print medians(li2)
    print medians(li3)