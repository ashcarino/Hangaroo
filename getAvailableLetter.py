import string
def getAvailableLetters(lettersGuessed):
    letters = string.ascii_lowercase
    for x in lettersGuessed:
    
        letters.remove(x)
        
    return ' '.join(letters)