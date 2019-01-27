"""Bottom-Up Merge Sort"""


def sort(L):
    """Sort the elements in list 'L' in ascending order."""
    L = [[i] for i in L]

    while len(L) > 1:
        aL = []
        to_merge = []

        for i in range(len(L)):
            to_merge.append(L[i])
            if i % 2 != 0:
                aL.append(merge(*to_merge))
                to_merge.clear()

        L = aL

    return L[0]


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
