def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    """Loop through secret word and for whatever letters are guessed in apple, print those letters and print an underscore for the letters outstanding"""

    this = []  # list to do shit in
    # set up our list to append and change into IE out default list
    for n in range(len(secretWord)):
        this.append("_")

    richard = 0  # richard is richard

    for n in secretWord:  # loop though secret word
        if n in lettersGuessed:  # if letter in secret word
            # this (index richard) will be replaced with value n
            this[richard] = n

        richard += 1  # update iteration

    Rword = " ".join(this)  # join words
    return Rword  # returns our word


print(getGuessedWord(secretWord='apple',
      lettersGuessed=['e', 'i', 'k', 'p', 'r', 's']))
