def getGuessedWord(secretWord,lettersGuessed):
    word = ''
    for x in secretWord:            
        if x in lettersGuessed:
            word += x
        else:
            word += '_ '
            
    return word