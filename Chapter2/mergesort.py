#Various mergesort implementations

from collections import deque

# an iterative mergesort using a queue
def mergesort(a):
    queue = []
    for val in a:
        queue.append([val])
    q = deque(queue)
    while(len(q) > 1):
        q.append(merge(q.popleft(),q.popleft()))
    return q.popleft()

# a recursive mergesort
def mergesort2(a):
    if len(a) > 1:
        b1 = int(len(a)/2)
        return merge(mergesort2(a[:b1]) , mergesort2(a[b1:]))

    else:
        return a

#  a recursive merge
def merge(a,b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    reval = []
    if(a[0] < b[0]):
        reval.append(a[0])
        return reval + merge(a[1:], b)
    else:
        reval.append(b[0])
        return reval + merge(a, b[1:])

# an iterative merge
def merge2(a,b):
    res = []
    i,j=0,0
    while(i < len(a) and j < len(b)):
        if(a[i] > b[j]):
            res.append(b[j])
            j += 1
        else:
            res.append(a[i])
            i += 1
    if(i == len(a)):
        return res + b[j:]
    else:
        return res + a[i:]




