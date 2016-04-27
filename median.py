import heapq

'''Fine median in running stream
requirements; min_heap and max_heap'''

'''Assume that the elements in the list 
are from the datastream'''
def medians(li):
    if len(li) <= 1:
        return li
    return _medians(li)
    
'''if the list is not empty
the datastream will begin with the loop;
          middle
max_heap          min_heap'''

def _medians(li):
    
    min_h = [] # right side
    max_h = [] # left side
    li_m = [] # collect the medians 
    
    for el in li:
        
        # The beginning of the case; el can be in max_h or min_h. It's your decision.
        if max_h == [] and min_h == []:
            temp = el
            heapq.heappush(max_h,el)
            # heapq._heapify_max(max_h)
        else:    
            
            #insert component
            mid = li_m[len(li_m)-1]
            
            if el <= mid:
                heapq.heappush(max_h,el)
            else:
                heapq.heappush(min_h,el)
        
            heapq._heapify_max(max_h)
            heapq.heapify(min_h)
            
            #adjust component
            if len(max_h) - len(min_h) > 1:
                temp = heapq.heappop(max_h)
                heapq.heappush(min_h,temp)
            elif len(min_h) - len(max_h) > 1:
                temp = heapq.heappop(min_h)
                heapq.heappush(max_h,temp)
            
            heapq.heapify(min_h)
            heapq._heapify_max(max_h)
            
            #determine the median component
            if len(max_h) == len(min_h):
                temp = (max_h[0] + min_h[0])/2.0
            elif len(max_h) - len(min_h) == 1:
                temp = max_h[0]
            elif len(min_h) - len(max_h) == 1:
                temp = min_h[0]
                
        li_m.append(temp)
        
    return li_m
    
if __name__ == "__main__":

    li = [5,3,4,1,6]
    print medians(li)
    # expected output >> [5,4,4,3.5,4]