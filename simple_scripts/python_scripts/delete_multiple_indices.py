"""Delete multiple indices from list at the same time."""

L = ['a', 'b', 'c', 'd', 'e', 'f']
indices_to_del = [1, 3, 5]

L = [i for (i, j) in enumerate(L) if j not in indices_to_del]
