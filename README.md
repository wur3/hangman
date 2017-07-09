# hangman
Simulates the classic game "Hangman" using CLI with Python.<br />
<br />
--TUTORIAL--<br />
First, you entire one word into "input.txt." As an example, "input.txt" has the word "alligator." The program will produce gallows as well as the word blanked out. For example, "alligator" would show:<br />
_ _ _ _ _ _ _ _ _<br /> 
From there on, you just guess letters to see if they fit in the word. If you enter the correct letter, it will be revealed in the blank lines. If the letter guessed is incorrect, the letter will be listed after: <br />
Incorrect:<br />
and the gallows will have parts of a man's body added onto it.<br />

If you complete the word before the hangman is completed, the game will print "Congratulations! You win!"<br />
If the hangman is completed (you guess the wrong letter 6 times), the game will print "GAME OVER! He got hung!"
