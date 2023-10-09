def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        print("mkm")
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while (i < len(left)):
        result.append(left[i])
        i += 1

    while (j < len(right)):
        result.append(right[j])
        j += 1

    return result


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        print("1")
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


bart = [6, 2, 1, 2, 3, 4]
kmart = [2, 3, 424, 234, 243, ]
print(kmart[kmart[0]])
