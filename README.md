#hangman

Simulates the classic game "Hangman" using CLI with Python.<br />
<br />
First, you need to enter the keyword that other people try to guess. However, because using 'input()' would leave the word on the CLI to easily be read, hangmanDriver.py takes the word in the file "input.txt". "input.txt" MUST contain one word only.<br />
From there on, you just guess letters to see if they fit in the word. If you enter the correct letter, it will be revealed in the blank lines. If the letter guessed is incorrect, the letter will be listed after: <br />
Incorrect:<br />
and the gallows will have parts of a man's body drawn on.<br />
