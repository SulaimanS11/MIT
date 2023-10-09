# # def score(word, f):
# #     """
# #        word, a string of length > 1 of alphabetical
# #              characters (upper and lowercase)
# #        f, a function that takes in two int arguments and returns an int

# #        Returns the score of word as defined by the method:

# #     1) Score for each letter is its location in the alphabet (a=1 ... z=26)
# #        times its distance from start of word.
# #        Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
# #     2) The score for a word is the result of applying f to the
# #        scores of the word's two highest scoring letters.
# #        The first parameter to f is the highest letter score,
# #        and the second parameter is the second highest letter score.
# #        Ex. If f returns the sum of its arguments, then the
# #            score for 'adD' is 12
# #     """

# alpha = "abcdefghijklmnopqrstuvwxyz"
# for k, v in enumerate(alpha):
#     if k == "k":
#         print(k, v)


# f = lambda x, y: x + y


# alpha = "abcdefghijklmnopqrstuvwxyz"
# word = "adD"
# lsword = [char for char in word.lower()]
# count = 0
# print(lsword)

# sums = {}
# for n in lsword:
#     count += 1
#     for k, v in enumerate(alpha):
#         if v == n:
#             if n in sums.keys():
#                 sums[f"{n}{count}"] = k+1
#             sums[n] = k+1


# while len(sums.keys()) > 2:
#     del sums[min(sums.keys())]

# vals = []

# for k
# # sums to f
# f()
# print(sums)

# def score(word, f):
#     scores = []
#     letters = "abcdefghijklmnopqrstuvwxyz"
#     alphabet = {}

#     for i in range(1, 27):
#         alphabet[letters[i - 1]] = i

#     for index, x in enumerate(word.lower()):
#         scores.append(alphabet[x] * index)
#     highest = 0

#     for i in range(len(scores)):
#         print(i)
#         if scores[i] == max(scores):
#             highest = scores.pop(i)
#     second_highest = 0

#     for i in range(len(scores)):
#         if scores[i] == max(scores):
#             second_highest = scores.pop(i)
#     return f(highest, second_highest)


def score(word, f):
    scores = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    alphabet = {}
    for i in range(1, 27):
        alphabet[letters[i - 1]] = i
    for index, x in enumerate(word.lower()):
        scores.append(alphabet[x] * index)
    highest = scores[0]
    second_highest = None
    for x in scores:
        if (second_highest == None or second_highest < x):
            second_highest = x
        elif (highest < x):
            if (second_highest == None or second_highest < highest):
                second_highest = highest
            highest = x
    return f(highest, second_highest)


print(score("WHooREESSES", lambda x, y: x+y))
