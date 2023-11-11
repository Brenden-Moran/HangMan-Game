# HangMan-Game

Overview:
The Python Hangman Game is an interactive program that brings the classic word-guessing game to life. Designed for user engagement, the program allows players to customize the difficulty by selecting the size of the word they want to guess and the number of lives they have for each game. The game dynamically selects a random word from a predefined dictionary, prompting users to guess letters until they either correctly identify the word or run out of lives.

Key Features:

User Input Customization:
The program provides users with the flexibility to customize the game difficulty by choosing the size of the word they wish to guess and setting the number of lives for each attempt.

Random Word Selection:
A random word is selected from a dictionary file, ensuring a diverse and unpredictable gaming experience. This feature adds an element of challenge and variety to each session.

Letter Guessing Mechanism:
Players input letters as guesses to uncover the hidden word. The program validates user input, handling both correct and incorrect guesses, and updates the display to reflect the current state of the word.

Lives System:
Users start each game with a predetermined number of lives. Incorrect guesses result in the deduction of a life. The game continues until the player correctly guesses the word or runs out of lives.

Game Over Handling:
If the player runs out of lives, the program prompts whether the user wants to play again. If the user chooses to continue, a new round begins with a fresh word and the specified number of lives.

Technical Details:

Programming Language: The program is written in Python, making use of its simplicity and versatility for interactive game development.
File Handling: Utilizes a dictionary file to source a pool of words for the game, enhancing replayability and variety.
User Input Validation: Implements robust input validation to ensure that user guesses are within the specified parameters and adhere to the game rules.
