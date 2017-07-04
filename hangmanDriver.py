from hangman import Hangman

h = Hangman("cherry")
turn = 1
keep_going = True
while(keep_going):
    print("\nTurn " + str(turn) + "--------------------------------------")
    user_guess = input("Guess a letter:\n")
    h.take_guess(user_guess)
    print(h.guy + "\n")
    print(" ".join(h.display) + "\n")
    print("Incorrect: " + ", ".join(h.bad_guess) + "\n")
    if(h.display == h.keyword):
        print("Congratulations! You win!")
        keep_going = False
    turn += 1