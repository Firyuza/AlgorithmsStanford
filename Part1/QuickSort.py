import numpy as np
import sys

sys.setrecursionlimit(1000000)

TOTAL_COMPARISONS = 0

def choose_pivot(A, l, r):
    # return l
    # return r - 1
    return l + int(np.floor((r - l) / 2))
    # indices = [l, int(np.floor(r - l) / 2), r - 1]
    # return indices[np.argsort(np.array(A)[indices])[1]]

def swap(A, i, j):
    temp = A[j]
    A[j] = A[i]
    A[i] = temp

    return

def partition_around_pivot(A, l, r, pivot_index):
    pivot = A[pivot_index]
    i = l + 1 if pivot_index == l else l
    for j in range(i, r, 1):
        if A[j] < pivot:
            swap(A, i, j)
            if i == pivot_index:
                pivot_index = j
            i += 1
    i = i - 1 if pivot_index == l else i
    swap(A, pivot_index, i)

    return i

def quick_sort(A, l, r):
    if (r - l) <= 1:
        return
    pivot_index = choose_pivot(A, l, r)

    global TOTAL_COMPARISONS
    TOTAL_COMPARISONS += (r - l) - 1
    pivot_index = partition_around_pivot(A, l, r, pivot_index)

    quick_sort(A, l, pivot_index)
    quick_sort(A, pivot_index + 1, r)

    return

with open('/Users/macbook/PycharmProjects/StanfordAlgorithms/Part1/data/QuickSort.txt', 'r') as f:
    content = f.read().strip()
    string_numbers = content.split('\n')
    a = np.array(string_numbers).astype(np.int32)
    quick_sort(a, 0, len(a))
    TOTAL_COMPARISONS = 0
    quick_sort(a, 0, len(a))
print(a)
print(TOTAL_COMPARISONS)

# TOTAL_COMPARISONS 162085 for first pivot
# TOTAL_COMPARISONS 147696 for median pivot
# TOTAL_COMPARISONS 160361 for final pivot
# TOTAL_COMPARISONS 148385 for median-of-three

