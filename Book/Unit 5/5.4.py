from re import L


def f(L1, L2):
    """L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""
    richard = list(map(lambda x, y: x**y, L1, L2))
    return sum(richard)


l1 = [2, 2, 2]
l2 = [2, 4, 2]
print(f(l1, l2))
