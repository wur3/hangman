from hangman import Hangman

input_file = open('./input.txt')
round = 1
for line in input_file:
    the_word = line.strip()
    h = Hangman(the_word)
    turn = 1
    while(True):
        print("Turn " + str(turn) + "--------------------------------------")
        h.print_guy()
        if(h.strikes >= 6):
            print(" ".join(h.keyword) + "\nGAME OVER! He got hung.")
            break
        print(" ".join(h.display) + "\n")
        if(h.display == h.keyword):
            print("Congratulations! You win!")
            h.bad_guess.clear()
            h.good_guess.clear()
            h.strikes=0
            break

        print("Incorrect: " + ", ".join(h.bad_guess) + "\n")
        user_guess = input("Guess a letter: ")
        while(user_guess in h.bad_guess or user_guess in h.good_guess):#no repeats
            user_guess = input("Guess a different letter: ")
        h.take_guess(user_guess)
        
        turn += 1
input_file.close()