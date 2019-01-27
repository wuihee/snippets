"""Naive Polynomial Multiplication"""


def remove_zeros(L):
    """Given a list 'L', remove all zeros in front."""
    while not L[0]:
        L = L[1:]

    return L


def multiply_polynomial(A, B):
    """
    Give 2 polynomials A and B, and their respective lengths n, find the
    product polynomial. Runtime: O(n) = n^2.
    """
    n = len(A)
    m = len(B)
    product = [0 for i in range(n + m - 1)]

    for a in range(n):
        for b in range(m):
            product[a + b] += A[a] * B[b]

    return remove_zeros(product)
