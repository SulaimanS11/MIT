import re
from ps4a import *


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # asks for input
    score = 0
    while True:
        print("Current Hand: ", end=' ')
        displayHand(hand)

        bob = input(
            "Enter word, or a \".\" to indicate that you are finished: ")

        if bob == '.':
            print("Goodbye! Total score: {} points.".format(score))
            return None

        elif isValidWord(bob, hand, wordList) == False:
            print("Invalid word, please try again.")
            continue

        else:
            smore = getWordScore(bob, n)
            score += smore
            print("\"{}\" earned {} points. Total: {} points".format(
                bob, smore, score))
            hand = updateHand(hand, bob)

            if calculateHandlen(hand) == 0:
                print("Run out of letters. Total score: {} points.".format(score))
                return None


wordlist = loadWords()
honda = {'n': 1, 'e': 1, 't': 1, 'a': 1, 'r': 1, 'i': 2}
# Enter word, or a "." to indicate that you are finished: him
# "him" earned 24 points. Total: 24 points
playHand(honda, wordlist, 7)
