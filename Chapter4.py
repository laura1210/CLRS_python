import math

# 4.1 Maximum subarray problem
def max_crossing_subarray(A, low, mid, high):
    '''
    Find the maximum subarray of A crossing mid point.

    Inputs:
    A: (list) the array to find the max crossing subarray
    low: (int) index start searching
    mid: (int) index must be included in the subarray (mid point)
    high: (int) index end searching

    Returns:
    max_left: (int) start index of the subarray
    max_right: (int) end index of the subarray
    total_sum: (float) sum of the subarray

    O(n)
    '''
    max_left = mid
    max_right = mid
    left_sum = - math.inf
    sum_ = 0
    for i in range(mid, low, -1):
        sum_ += A[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i

    right_sum = - math.inf
    sum_ = 0
    for i in range(mid, high, 1):
        sum_ += A[i]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = i

    total_sum = left_sum + right_sum
    return max_left, max_right, total_sum


def max_subarray(A, low, high):
    '''
    Returns:
    low: (int) start index
    high: (int) end index
    sum: (float) sum of max subarray

    O(nlg(n))
    '''
    if low == high:
        return (low, high, A[low])

    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_sum = max_subarray(A, low, mid)
        right_low, right_high, right_sum = max_subarray(A, mid+1, high)
        cro_low, cro_high, cro_sum = max_crossing_subarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cro_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cro_sum:
            return right_low, right_high, right_sum
        else:
            return cro_low, cro_high, cro_sum



# 4.2 Matrix multiplication
def simple_matrix_multiply(A, B):
    # O(n^3)
    n = len(A)
    C = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            c_ij = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


