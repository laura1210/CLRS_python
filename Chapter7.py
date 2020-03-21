import random

# 7.1 Quicksort
def partition(A, p, r):
    # return q
    # O(n)
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A_i = A[i]
            A[i] = A[j]
            A[j] = A_i
    A_r = A[r]
    A[r] = A[i+1]
    A[i+1] = A_r
    return i+1

def quicksort(A, p=None, r=None):
    # some modification
    if p is None:
        p = 0
    if r is None:
        r = len(A) - 1
    # core code
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


# 7.3 Randomized version
def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A_i = A[i]
    A[i] = A[r]
    A[r] = A_i
    return partition(A, p, r)

def randomized_quicksort(A, p=None, r=None):
    if p is None:
        p = 0
    if r is None:
        r = len(A) - 1
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1)
        randomized_quicksort(A, q+1, r)