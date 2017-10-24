from hangman import Hangman

input_file = open('./input.txt')
the_word = input_file.read()
input_file.close()
h = Hangman(the_word)
turn = 1
while(True):
    print("\nTurn " + str(turn) + "--------------------------------------")
    h.print_guy()
    if(h.strikes >= 6):
        print(" ".join(h.keyword) + "\nGAME OVER! He got hung.")
        break
    print(" ".join(h.display) + "\n")
    if(h.display == h.keyword):
        print("Congratulations! You win!")
        break

    print("Incorrect: " + ", ".join(h.bad_guess) + "\n")
    user_guess = input("Guess a letter: ")
    while(user_guess in h.bad_guess or user_guess in h.good_guess):#no repeats
        user_guess = input("Guess a different letter: ")
    h.take_guess(user_guess)
    
    turn += 1