import heapq

'''
Fine median in running stream
requirements; min_heap and max_heap
'''

'''
Assume that the elements in the list 
are from the datastream
'''
def medians(li):
    if len(li) <= 1:
        return li
    return _medians(li)
    
'''
if the list is not empty
the datastream will begin with the loop;
          middle = [5,4]
max_heap          min_heap
   3                  5         
'''

#get the median in the list
def push_median(max_h,min_h,el,mid):
    if el <= mid:
        heapq.heappush(max_h,el)
    else:
        heapq.heappush(min_h,el)

#adjust the heap if one of the heap size
#is greater than the other one by more than 1
def adjust_heap(max_h,min_h):
    if len(max_h) - len(min_h) > 1:
        temp = heapq.heappop(max_h)
        heapq.heappush(min_h,temp)
    elif len(min_h) - len(max_h) > 1:
        temp = heapq.heappop(min_h)
        heapq.heappush(max_h,temp)
            
#get the final median from two heap tree
def get_median(max_h,min_h):
    if len(max_h) == len(min_h):
        temp = (max_h[0] + min_h[0])/2.0
    elif len(max_h) - len(min_h) == 1:
        temp = max_h[0]
    elif len(min_h) - len(max_h) == 1:
        temp = min_h[0]
    return temp

#heapify the both min and max tree
def _heapify(max_h,min_h):
    heapq._heapify_max(max_h)
    heapq.heapify(min_h)
            
#return list of medians
def _medians(li):
    
    min_h = [] # right side
    max_h = [] # left side
    li_m = [] # collect the medians 
    
    for el in li:
        
        #1) The beginning of the case; el can be in max_h or min_h. It's your decision.
        if max_h == [] and min_h == []:
            temp = el
            heapq.heappush(max_h,el)
        else:    
            
            #2)get the median from the median list component
            mid = li_m[len(li_m)-1]
            
            #3)push the element into the heap
            push_median(max_h,min_h,el,mid)
            _heapify(max_h,min_h)        
            
            #4)adjust both min and max tree to have difference of 1 
            adjust_heap(max_h,min_h)
            _heapify(max_h,min_h)        
            
            #5)determine the median component
            temp = get_median(max_h,min_h)
          
        #6)Finally, when the decision is made that which value should be the median
        #then added it to the median list
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