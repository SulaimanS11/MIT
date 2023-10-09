def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    freq = {}
    lost = []

    if "{}\n".format(word.upper()) in wordlist:
        lost.append(1)
    else:
        return False

    for n in word:
        if hand.get(n, 0) == 0:
            return False

    for x in word:
        freq[x] = freq.get(x, 0) + 1

    for n in word:
        if n in hand:
            lost.append(1)
        else:
            print("word prob")
            lost.append(0)

    for n in freq:
        if freq[n] <= hand[n]:
            lost.append(1)
        else:
            print("freq prob")
            lost.append(0)

    if 0 in lost:
        return False
    else:
        return True


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    return sum(hand.values())


wordlist = open("P\\MIT\\pset4\\words.txt", "r")
hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
print(isValidWord("honey", hand, wordlist))

print(calculateHandlen(hand))
