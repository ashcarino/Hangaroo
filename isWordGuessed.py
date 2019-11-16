def isWordGuessed(secretWord,lettersGuessed): 
    for x in secretWord:
        
        if x in lettersGuessed:
            return ("true")
        else:
            return ("false")

