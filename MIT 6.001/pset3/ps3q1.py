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


print(isWordGuessed("apple", lettersGuessed=[
      'a', 'p', 't', 'l', 'e', 'e', 'q']))
