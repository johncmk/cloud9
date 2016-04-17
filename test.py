import random

def shuffle_li(li):
    if len(li) <= 1:
        print "nothing to shuffle"

    for i in range(len(li)-1,-1,-1):
        ptr = random.randrange(i+1)
        li[i],li[ptr] = li[ptr],li[i]
    return li

def qsort(li):
    if li == []:
        return li
    pivot = random.choice(li)
    l,eq,r = [],[],[]
    for el in li:
        if el < pivot:
            l.append(el)
        elif el > pivot:
            r.append(el)
        else:
            eq.append(el)
    return qsort(l) + eq + qsort(r)



if __name__ == "__main__":
 
    li = shuffle_li(range(1000))

    print "shuffle : ",li
    print "QuickSort : ",qsort(li)