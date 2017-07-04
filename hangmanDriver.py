from hangman import Hangman

h = Hangman("cherry")
keep_going = True
while(keep_going):
    user_guess = input("Guess a letter:\n")
    h.take_guess(user_guess)
    print(" ".join(h.display))
    print("Incorrect: " + ", ".join(h.bad_guess))
    if(h.display == h.keyword):
        print("Congratulations! You win!")
        keep_going = False