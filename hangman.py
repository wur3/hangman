class Hangman:
    guy = "  _______\n |/      |\n |      (_)\n |      \|/\n |       |\n |      / \\\n |\n_|___"
    bad_guess = [] #list of wrongly-guessed letters
	strikes = 0 #at 6 strikes, the hangman is completed and the game ends
    def __init__(self, word):
        self.keyword = list(word) #list that stores the word that is being guessed
        self.display = list('_' * len(word)) #list that starts out as the number-of-letters-in-the-word amount of blank lines e.g. 'cat' -> ['_', '_', '_']
    def take_guess(self, guess):
        if guess not in self.keyword:
            self.bad_guess.append(guess)
			strikes += 1
        else:
            i = 0
            while(i != len(self.keyword)):
                try:
                    x = self.keyword[i:].index(guess) #index value where the letter is found
                except ValueError:
                    break
                self.display[x+(len(self.keyword)-len(self.keyword[i:]))] = guess #compensates for shift in indices values for keyword versus keyword[i:]
                i+=1
    def print_guy(self):
        print(self.guy)
    def print_bad_guess(self):
        print(self.bad_guess)
