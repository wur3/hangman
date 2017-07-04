class Hangman:
    guy = "  _______\n |/      |\n |      (_)\n |      \|/\n |       |\n |      / \\\n |\n_|___"
    bad_guess = [] #list of wrongly-guessed letters
	
    def __init__(self, word):
        self.keyword = list(word) #list that stores the word that is being guessed
        self.display = list('_' * len(word)) #list that starts out as the number-of-letters-in-the-word amount of blank lines e.g. 'cat' -> ['_', '_', '_']
    def take_guess(self, guess):
        if guess not in self.keyword:
            self.bad_guess.append(guess)
        else:
            x = self.keyword.index(guess)
            self.display[x] = guess
    def print_guy(self):
        print(self.guy)
    def print_bad_guess(self):
        print(self.bad_guess)
