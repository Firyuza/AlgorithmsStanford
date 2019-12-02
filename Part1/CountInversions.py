import numpy as np

with open('/Users/macbook/Downloads/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt', 'r') as f:
    lines = f.readlines()
a = np.zeros((len(lines)))
for id, line in enumerate(lines):
    a[id] = int(line.strip())

def count_sorted(A, n):
    if n == 1:
        return A, 0
    half_part = int(np.ceil(n/2))
    B, x = count_sorted(A[:half_part], len(A[:half_part]))
    C, y = count_sorted(A[half_part:], len(A[half_part:]))
    D, z = merge_and_count_split_inversions(B, C)

    return D, x + y + z

def merge_and_count_split_inversions(B, C):
    D = np.zeros((len(B) + len(C)))
    i = 0
    j = 0
    count_inversions = 0
    for k in range(len(D)):
        if (j == len(C)) or (i < len(B) and B[i] < C[j]):
            D[k] = B[i]
            i += 1
        else:
            D[k] = C[j]
            j += 1
            count_inversions += len(B[i:]) if i < len(B) else 0

    return D, count_inversions

out, count_inv = count_sorted(a, len(a))
print(count_inv) # 2407905288