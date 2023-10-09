from ps4a import *


# def playGame(wordList):
#     """
#     Allow the user to play an arbitrary number of hands.

#     1) Asks the user to input 'n' or 'r' or 'e'.
#       * If the user inputs 'n', let the user play a new (random) hand.
#       * If the user inputs 'r', let the user play the last hand again.
#       * If the user inputs 'e', exit the game.
#       * If the user inputs anything else, tell them their input was invalid.

#     2) When done playing the hand, repeat from step 1
#     """

#     bob = 0
#     while True:
#         rango = input(
#             "Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
#         if rango == "n":
#             carl = dealHand(HAND_SIZE)
#             playHand(carl, wordList, HAND_SIZE)
#             bob = 1

#         elif rango == "r" and bob == 0:
#             print("You have not played a hand yet. Please play a new hand first!")
#             print()
#             continue
#         elif rango == "r":
#             playHand(carl, wordList, HAND_SIZE)
#         elif rango == "e":
#             return 0
#         else:
#             print("Invalid command.")


# wordlist = loadWords()
# honda = {'n': 1, 'e': 1, 't': 1, 'a': 1, 'r': 1, 'i': 2}
# # Enter word, or a "." to indicate that you are finished: him
# # "him" earned 24 points. Total: 24 points
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular l.etter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


dealHand(7)
# playGame(wordlist)
