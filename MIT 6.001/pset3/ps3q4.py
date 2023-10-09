def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    def isWordGuessed(secretWord, lettersGuessed):
        '''
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far
        returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
        '''
        set_word = set(secretWord)
        lenset_word = len(set_word)
        rightCount = 0

        for n in set(lettersGuessed):
            if n in set_word:
                rightCount += 1

        if rightCount == len(set_word):
            return True
        else:
            return False

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

    def getAvailableLetters(lettersGuessed):
        '''
        lettersGuessed: list, what letters have been guessed so far
        returns: string, comprised of letters that represents what letters have not
        yet been guessed.
        '''
        # FILL IN YOUR CODE HERE...

        alpha = "abcdefghijklmnopqrstuvwxyz"
        beta = ''

        for n in alpha:
            if n not in lettersGuessed:
                beta += n

        return beta

    print(("""Loading word list from file...\n55900 words loaded.\nWelcome to the game Hangman!\nI am thinking of a word that is {} letters long.\n-----------""").format(len(secretWord)))

    guessesleft = 8
    lettersGuessed = []
    guess = ""
    while True:
        # PROMT FOR INPUT
        # IF INPUT CORRECT UPDATE getGuessedWord and getAvailableLetters Else -= guessesleft
        print(("You have {} guesses left.").format(guessesleft))
        print("Available letters: ", end="")
        print(getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")

        if guess in lettersGuessed:  # if guess guessed before
            print("Oops! You've already guessed that letter: ", end="")
            print(getGuessedWord(secretWord, lettersGuessed))

        # if not guessed before and wrong append to letters guessed
        elif guess not in secretWord and guess not in lettersGuessed:
            guessesleft -= 1
            lettersGuessed.append(guess)
            print("Oops! That letter is not in my word: ", end="")
            print(getGuessedWord(secretWord, lettersGuessed))

        elif guess in secretWord:  # good guess in and not in
            lettersGuessed.append(guess)
            print("Good guess: ", end="")
            print(getGuessedWord(secretWord, lettersGuessed))

        if guessesleft == 0:
            print("-----------")
            print("Sorry, you ran out of guesses. The word was {}.").format(
                secretWord)
            break

        if isWordGuessed(secretWord, lettersGuessed):
            print("-----------")
            print("Congratulations, you won!")
            break

        print("-----------")


hangman(secretWord="tact")
