"""Counting Sort"""


def counting_sort(L, m):
    """
    The counting sort algorithm is a non-comparison based sorting
    algorithm that sorts asymptotically less than big-omega(nlogn).
    However, some pre-existing information must be provided, in the
    form of the parameter m, which indicates that the elements in L
    range from 0 to m.
    """
    n = len(L)
    count = [0 for _ in range(m + 1)]
    positions = [0 for _ in range(m + 1)]
    output = [0 for _ in range(n)]

    # Construct Histogram
    for i in range(n):
        count[L[i]] += 1

    # Starting Positions
    for i in range(1, m + 1):
        positions[i] = positions[i - 1] + count[i - 1]
    print(positions)

    # Output
    for i in range(n):
        output[positions[L[i]]] = L[i]
        positions[L[i]] += 1

    return output
