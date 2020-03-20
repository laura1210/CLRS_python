import math

# 2.1 Insertion sort O(n^2)
def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A

# 2.2-2 Selection sort O(n^2)
def selection_sort(A):
    for i in range(len(A)-1):
        index = i
        value = A[i]
        for j in range(i,len(A)):
            if A[j] < A[i]:
                index = j
                value = A[j]
        A[index] = A[i]
        A[i] = value
    return A

# 2.3 Divide-and-conquer approach O(nlg(n))
def merge(A, n):
    L = A[:n] + [math.inf]
    R = A[n:] + [math.inf]
    i = 0
    j = 0
    for k in range(len(A)):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def merge_sort(A):
    if len(A) > 1:
        n = len(A) // 2
        merge_sort(A[:n])
        merge_sort(A[n:])
        merge(A,n)
    return A