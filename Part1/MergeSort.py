import numpy as np

def merge(A, B):
    C = np.zeros((len(A) + len(B)))
    i = 0
    j = 0
    for k in range(len(C)):
        if (j == len(B)) or (i < len(A) and A[i] < B[j]):
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1

    return C

def merge_sort(X):
    n = len(X)
    if n == 1:
        return X
    half = n // 2 if n % 2 == 0 else (n // 2 + 1)
    A = merge_sort(X[:half])
    B = merge_sort(X[half:])
    C = merge(A, B)

    return C

a = np.arange(0, 6, 1)
b = np.arange(2, 8, 1)
c = merge(a, b)
print(c)