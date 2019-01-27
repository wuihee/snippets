"""Top-Down Merge Sort"""


def sort(L):
    """Sort the elements in list 'L' in ascending order."""
    n = len(L)
    L1 = L[:n // 2]
    L2 = L[n // 2:]

    # Base Cases
    if n == 2:
        return merge(L1, L2)
    elif n == 3:
        return merge(L1, sort(L2))

    return merge(sort(L1), sort(L2))


def merge(L1, L2=[]):
    """
    Return a merged list consisting of elements sorted in ascending
    order from sorted lists 'L1' and 'L2'.
    """
    if not L2:
        return L1

    L3 = []

    while L1 and L2:
        n = L1.pop(0) if L1[0] < L2[0] else L2.pop(0)
        L3.append(n)

    L3.extend(L1) if not L2 else L3.extend(L2)

    return L3
