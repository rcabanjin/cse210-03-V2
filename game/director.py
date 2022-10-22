from guesser import guesser
from secret_word import SecretWord
from jumper import Display

# class that handles the game events
class Director:
    # Director class will control the sequence of play.

    # sources / parts if game is:
    def __init__(self):
        self.wordToGuess = self.wordGuess()
        self.chance = 0
        self.correct = 0
        self.index = -1
        self.letter = ''
        self.display = Display()

    # Starts the game by running by calling the main class
    def start_game(self):
        self._get_inputs()

    # function to get random word
    def wordGuess(self):
        random_word = SecretWord()
        word = random_word.word
        return word

    # call the classes created for getting the guesser's input letter
    def _get_inputs(self):
        #display correct guessed letter
        self.display.displayLetters(self.index, self.letter)
        # display parachute
        self.display.display_parachute(self.chance)
        # ask for user guess letter
        playerGuess = input("Enter a letter guess [a-z]: ")
        #check if user input is not a number and the length is 1
        if not (playerGuess.isdigit()) and len(playerGuess) == 1:
            #call class guesser
            guess = guesser(playerGuess, self.wordToGuess)
            match, self.index, self.letter, self.wordToGuess = guess.checkLetter()
            #check result if inputted letter match the letter in the word to be guessed
            if match == 1:
                self.correct += 1
                if self.correct < 5:
                    #contnue to ask input
                    self._get_inputs()
                else:
                    # the user guessed all the letters
                    self.display.displayLetters(self.index, self.letter)
                    self.display.display_parachute(self.chance)
                    print("Congratulation, You've guessed the word.")
                    exit()
            else:
                # if wrong guess
                self.chance += 1
                if self.chance < 5:
                    # contnue to ask input
                    self._get_inputs()
                else:
                    # if user reached the maximum of 5 guessing chance
                    self.display.displayLetters(self.index, self.letter)
                    self.display.display_parachute(self.chance)
                    print("Sorry, You've lost the game")

        else:
            #prompt when user inputted a number or the length of input is not 1
            print("Please enter a letter, not a number")
            self._get_inputs()

    # call the classes created for showing the guesser input letters and remaining characters
start = Director()
start.start_game()
