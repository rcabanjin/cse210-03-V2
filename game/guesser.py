
class guesser:
    def __init__(self, playerGuess, wordToGuess):
        self.guess = playerGuess
        self.wordToGuess = wordToGuess
    # check if guess letter match the word to be guessed
    def checkLetter(self):
        # if match
        if self.guess.lower() in self.wordToGuess:
            isMatch = 1
            #find the index of the guessed letter in the word to be guessed
            guessIndex = self.wordToGuess.index(self.guess)
            # replace the guessed letter with - so that it will not result to run time error
            # when the letter is inputted again
            newWord = self.wordToGuess[:guessIndex] + '-' + self.wordToGuess[guessIndex + 1:]
            return isMatch, guessIndex,self.guess.lower(), newWord

        else:
            isMatch = 0
            return isMatch, -1, '', self.wordToGuess



