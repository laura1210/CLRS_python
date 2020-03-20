import math

# 6.1 Heaps
def left(i):
    return (i + 1) * 2 - 1

def right(i):
    return (i + 1) * 2

def parent(i):
    return int((i + 1) / 2) - 1

# 6.2 Maintaining the heap property
def max_heapify(A, i):
    # assume the binary trees rooted at left(i) and right(i) are max-heaps
    # but A[i] might be smaller than its childern
    # O(lg(n))
    l = left(i)
    r = right(i)
    if l <= len(A) - 1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A) - 1 and A[r] > A[largest]:
        largest = r
    if i != largest:
        A_i = A[i]
        A[i] = A[largest]
        A[largest] = A_i
        max_heapify(A, largest)

# 6.3 Building a heap
def build_max_heap(A):
    # O(n)
    for i in range(parent(len(A) - 1), -1, -1):
        print(i)
        max_heapify(A, i)

# 6.4 Heapsort
def heap_sort(A):
    # O(nlg(n))
    sorted_A = []
    for i in range(len(A) - 1, 0, -1):
        sorted_A.append(A[0])
        A[0] = A[i]
        del A[i]
        max_heapify(A, 0)
        print(A)
    return sorted_A

# 6.5 Priority queue
# heap can support any priority-queue operation in O(lg(n)) time
def heap_maximum(A):
    # A is a max-heap
    # returns the largest element
    return A[0]

def heap_extract_max(A):
    # removes and returns the largest element
    # while keep A as a max-heap
    if len(A) < 1:
        print('heap underflow')
        return None
    max = A[0]
    fin = len(A) - 1
    A[0] = A[fin]
    del A[fin]
    max_heapify(A, 0)
    return max

def heap_increase_key(A, i, key):
    # increases the value of element i to key
    if A[i] > key:
        print('new key is smaller than current key')
        return None
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A_i = A[i]
        A[i] = A[parent(i)]
        A[parent(i)] = A_i
        i = parent(i)

def max_heap_insert(A, key):
    # inserts value key into A
    A.append(-math.inf)
    heap_increase_key(A, len(A) - 1, key)