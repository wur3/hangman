# hangman
Simulates the classic game "Hangman" on the command line.<br />
<br />
First, you enter one word into "input.txt." As an example, "input.txt" has the word "alligator." The program will display gallows followed by blanks to show how many letters in the word. For example, "alligator" would show:<br />
<br />
_ _ _ _ _ _ _ _ _<br /> 
From there on, you just guess letters to see if they fit in the word. If you enter the correct letter, it will be revealed in the blank lines. If the letter guessed is incorrect, the letter will be listed after: <br />
Incorrect:<br />
and the gallows will have parts of a man's body added onto it.<br />

If you complete the word before the hangman is completed, the game will print "Congratulations! You win!"<br />
If the hangman is completed (you guess the wrong letter 6 times), the game will print "GAME OVER! He got hung!"
