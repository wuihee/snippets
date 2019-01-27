"""Selection Sort"""


def selection_sort(L):
    """
    Given list 'L', sort all items within in ascending order.
    """
    length = len(L)

    for i in range(length):
        # Find the index of the smallest number.
        s = i
        for j in range(i, length):
            if L[j] <= L[s]:
                s = j
        # Swap
        L[i], L[s] = L[s], L[i]

    return L
