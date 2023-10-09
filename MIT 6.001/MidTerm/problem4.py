# def getSublists(L, n):
#     listnums = (len(L)-n) - 1
#     lists = []
#     number = 0
#     while number < listnums:


# list len 5, 2 n = 2,3,4,5 4 iterations
# list len 10, 4 n = 4,5,6,7,8,9,10 7 iterations
# (len(L) - n) + 1


def getSublist(L, n):
    result = []
    for x in range((len(L) - n) + 1):
        result.append(L[x:x+n])
    return result


print(getSublist(L=[1, 1, 1, 1, 4], n=2))
