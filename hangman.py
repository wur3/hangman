class Hangman:
    guy = []
    guy.append("  _______\n |/      |\n |         \n |      \n |       \n |      \n |\n_|___") #empty
    guy.append("  _______\n |/      |\n |      (_)\n |         \n |        \n |          \n |\n_|___") #head
    guy.append("  _______\n |/      |\n |      (_)\n |       | \n |       |\n |          \n |\n_|___") #body
    guy.append("  _______\n |/      |\n |      (_)\n |      \\| \n |       |\n |          \n |\n_|___") #left-arm
    guy.append("  _______\n |/      |\n |      (_)\n |      \\|/\n |       |\n |          \n |\n_|___") #right-arm
    guy.append("  _______\n |/      |\n |      (_)\n |      \\|/\n |       |\n |      /   \n |\n_|___") #left-leg
    guy.append("  _______\n |/      |\n |      (_)\n |      \\|/\n |       |\n |      / \\\n |\n_|___") #left-leg
    guy.append("  _______\n |/      |\n |      (_)\n |      \\|/\n |       |\n |      / \\\n |\n_|___") #full
    bad_guess = [] #list of wrongly-guessed letters
    good_guess = [] #sublist of keyword, used to check for repeats
    strikes = 0 #at 6 strikes, the hangman is completed and the game ends
    def __init__(self, word):
        self.keyword = list(word) #list that stores the word that is being guessed
        self.display = [];
        for i in range(0,len(word)):
            if(self.keyword[i]!=' '):
                self.display.append('_');
            else:
                self.display.append(' ');
    def take_guess(self, guess):
        if guess not in self.keyword:
            self.bad_guess.append(guess)
            self.strikes += 1
        else:
            self.good_guess.append(guess)
            i = 0
            while(i != len(self.keyword)):
                try:
                    x = self.keyword[i:].index(guess) #index value where 'guess' is found in 'keyword'
                except ValueError:
                    break
                self.display[x+(len(self.keyword)-len(self.keyword[i:]))] = guess #compensates for shift in indices values for keyword versus keyword[i:]
                i+=1
    def print_guy(self): #print hangman guy
        print(self.guy[self.strikes])
    def print_bad_guess(self): #print list of wrong guesses
        print(self.bad_guess)
