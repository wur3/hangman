from hangman import Hangman

input_file = open('./input.txt')
the_word = input_file.read()
input_file.close()
h = Hangman(the_word)
turn = 1
keep_going = True
while(keep_going):
    print("\nTurn " + str(turn) + "--------------------------------------")
    user_guess = input("Guess a letter: ")
    while(user_guess in h.bad_guess or user_guess in h.good_guess):#no repeats
        user_guess = input("Guess a different letter: ")
    h.take_guess(user_guess)
    h.print_guy()
    if(h.strikes >= 6):
        print("GAME OVER! He got hung.")
        keep_going = False
        break
    print(" ".join(h.display) + "\n")
    print("Incorrect: " + ", ".join(h.bad_guess) + "\n")
    if(h.display == h.keyword):
        print("Congratulations! You win!")
        keep_going = False
    turn += 1