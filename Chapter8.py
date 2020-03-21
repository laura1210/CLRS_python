# 8.2 Counting sort O(n)
def counting_sort(A, k):
    # assume elements in A are integers in the range of 0 to k
    B = [None] * len(A)
    C = [0] * (k + 1)
    for j in range(len(A)):
        C[A[j]] += 1
    # C[i] now contains the number of elements equal to i
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    # # C[i] now contains the number of elements less than or equal to i
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B