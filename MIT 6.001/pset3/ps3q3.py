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


peen = []
print(getAvailableLetters(peen))
