from hangman import Hangman

h = Hangman("cherry")
h.take_guess('c')
h.take_guess('h')
h.take_guess('i')
print(h.bad_guess)
print(" ".join(h.display))
