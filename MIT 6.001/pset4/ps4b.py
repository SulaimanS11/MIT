from ssl import HAS_NEVER_CHECK_COMMON_NAME
from ps4a import *
import time


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

#
# Computer plays a hand
#


def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0):
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)):
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) +
                      ' points. Total: ' + str(totalScore) + ' points')
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')


#
# Problem #6: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1    
    """

    bob = 0

    while True:
        # enter n r e
        rango = input(
            "Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if rango != "r" and rango != "n" and rango != "e":
            print("Invalid Command.")
            print()
            continue
        elif rango == "r" and bob != 1:
            print("You have not played a hand yet. Please play a new hand first!")
            print()
            continue
        elif rango == "e":
            return None
        print()

        # enter U or C
        mango = input(
            "Enter u to have yourself play, c to have the computer play: ")
        while mango != "c" and mango != "u":
            print("Invalid Command.")
            print()
            mango = input(
                "Enter u to have yourself play, c to have the computer play: ")
        print()

        # u ==
        if rango == "n" and mango == "c":
            carl = dealHand(HAND_SIZE)
            compPlayHand(carl, wordList, HAND_SIZE)
            bob = 1
        elif rango == "n" and mango == "u":
            carl = dealHand(HAND_SIZE)
            playHand(carl, wordList, HAND_SIZE)
            bob = 1

        elif rango == "r" and mango == "u":
            playHand(carl, wordList, HAND_SIZE)
        elif rango == "r" and mango == "c":
            compPlayHand(carl, wordList, HAND_SIZE)
        elif rango == "e":
            return None

        # if mango == "c":
        #     carl = dealHand(HAND_SIZE)
        #     compPlayHand(carl, wordList, HAND_SIZE)
        # elif mango == "u"

        # if rango == "n":
        #     carl = dealHand(HAND_SIZE)
        #     playHand(carl, wordList, HAND_SIZE)
        #     bob = 1

        # elif rango == "r" and bob == 0:
        #     print("You have not played a hand yet. Please play a new hand first!")
        #     print()
        #     continue
        # elif rango == "r":
        #     playHand(carl, wordList, HAND_SIZE)
        # elif rango == "e":
        #     return None
        # else:
            print("Invalid command.")


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
