def isWordGuessed(secretWord,lettersGuessed): 
    for x in secretWord:
        if x in lettersGuessed:
            return ("true")
        else:
            return ("false")
def getGuessedWord(secretWord,lettersGuessed):
    word = ''
    for x in secretWord:            
        if x in lettersGuessed:
            word += x
        else:
            word += '_ '
            
    return word
def getAvailableLetters(lettersGuessed):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for x in lettersGuessed:    
        letters.remove(x)        
    return ' '.join(letters)
secretWord = "bardong"
def Hangaroo(secretWord):
    L = str(len(secretWord))
    mistakes = 4
    answer = str
    wordGuess = False
    lettersGuessed = []
    print ('Lets play Hangaroo')
    print ("You have to guess a word that is " + L, "letters long.")
  
    while mistakes > 0 and mistakes <= 4 and wordGuess is False:
         if secretWord == getGuessedWord(secretWord, lettersGuessed):
             wordGuess= True
             break
         print ('You have ' + str(mistakes), 'guesses left.')
         print ('Available letters: ')
         print(getAvailableLetters(lettersGuessed))
         answer = input('Please guess a letter: ').lower()
         if answer in secretWord:
             if answer in lettersGuessed:
                print ("Ouch! You already guessed that letter. ")
                print (getGuessedWord(secretWord, lettersGuessed))
                
             else:
                lettersGuessed.append(answer)
                print ('Good guess: ') 
                print (getGuessedWord(secretWord, lettersGuessed))
               
         else:
             if answer in lettersGuessed:
                print ("Ouch! You already guessed that letter. Please try again: ") 
                print (getGuessedWord(secretWord, lettersGuessed))
                
             else:
                lettersGuessed.append(answer)
                mistakes -= 1
                print ('Ouch! That letter is not in my word: ') 
                print (getGuessedWord(secretWord, lettersGuessed))
               
    if wordGuess == True:
        return 'Congratulations, you won!'
    elif mistakes == 0:
        print ('You ran out of guesses. The word was ') 
        print (secretWord)