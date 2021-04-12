def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break
# 创建最大堆
    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

# 堆排序
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst

if __name__ == "__main__":
    l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    heap_sort(l)
    print(l)
    
def heapify(tree, n, i):
    print(n,i)
    if i>=n:
        return
    
    c1 = 2*i + 1
    c2 = 2*i + 2
    m = i
    if c1<n and tree[c1]>tree[m]:
        m = c1
    if c2<n and tree[c2]>tree[m]:
        m = c2
    if m!=i:
        tree[m], tree[i] = tree[i], tree[m]
        heapify(tree, n, m)
        
if __name__ == "__main__":
    tree = [4, 10, 3, 5, 1, 2]
    n = 6
    heapify(tree, n, 0)
    print(tree)

import heapq as hq
def cookies(k, A):
    count = 0
    l = []
    for i in A:
        hq.heappush(l, i)
        
    while any(j<k for j in l) and len(l)>1:
        a = hq.heappop(l)
        b = hq.heappop(l)
        new = a + 2*b
        hq.heappush(l, new)
        count += 1
    if all(j>=k for j in l):
        return count
    else:
        return -1
    
def cookies(k, A):
    trys = 0
    heapq.heapify(A)
    while len(A)>1 and A[0]<=k:
        a = A[0]
        heapq.heappop(A)
        b = A[0]
        heapq.heappop(A)
        heapq.heappush(A, a+2*b)
        trys = trys + 1
    return trys if A[0] >=k else -1
    import heapq as hq
#========================================================================================
a = [[5,3,6,1,8,15,13,7,2,10], [5,3,6,1,8,15,13,7,2,10], [5,3,6,1,8,15,13,7,2,10]]
b = []
for i in range(len(a)):
    b += [item*(-1) for item in a[i]]
    print(b)
    hq.heapify(b)
    hq.heappop(b)
    print(b)
    
import heapq
def TopKIntegerSequence(matrix):
    # Write your code here
    H = []
    ans = []

    szlimit = len(matrix)
    for row in matrix:
        for e in row:
            heapq.heappush(H, e)
        ans.append(heapq.heappop(H))

    return ans