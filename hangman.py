
# author: (Brenden Moran)
# date: (1/18/23)
# file: hangman.py is a program that allows the user to play a game of hangman.
# input: A series of letters corrisponding to a word which the user has to guess.
# output: Outputs whether the letter is in the word which the user must guess as well as 
#         tells the user whether they won by guessing all of the correct letters to make the word.

from random import choice, random

   # make a dictionary.txt in the same folder where hangman.py is located
with open("dictionary.txt", "r") as dictionary_file:
  dictionary_file = dictionary_file.read()
  dictionary_file = dictionary_file.split() #creates a list of the txt file

dictionary_file = sorted(dictionary_file, key = lambda x:len(x), reverse = True) #Sorts by length of word


def import_dictionary (dictionary_file) :                 # Creates a dictionary with keys as numbers and vqalues as lists of words
    dictionary = {}
    max_size = 12
    try :
        while max_size > 1:                               # Creates keys of letters from 12-1 and values of empty lists               
          dictionary[(max_size)] = []
          max_size -= 1
        max_size = 12
        for word in dictionary_file:                      # Goes through all the words in the dictionary 
          if len(word) >= max_size:                       # and adds them to specific dictionary lists(values) based off of there lengths(keys)
            dictionary[(max_size)].append(word.upper())
          else:
            dictionary[(max_size)-1].append(word.upper())
            max_size -= 1                                 # Keeps the dictionary going through all of the keys

    except ValueError :                                   # will run if no dictionary with words is found
        print("No alphebet dictionary file found")
    return dictionary



def get_game_options () :                                                                         # Gets game options from user.
  try:
      size = int(input("Please choose a size of a word to be guessed [3-12, default any size]: \n")) # Sets the desired size of the word
      if size >= 3 and size <= 12:
        print("The word size is set to", size)
      else: 
        size = choice(range(3, 13))                                                                 # Randomly chooses a word size
        print("A dictionary word of any size will be chosen.")
  except ValueError:
      size = choice(range(3, 13))
      print("A dictionary word of any size will be chosen.")                                     # Runs if the value recieved is not an integer

  try:
      lives = int(input("Please choose a number of lives [1-10, default 5]: \n"))                     # Sets the desired amount of lives
      if lives >= 1 and lives <= 10:
        print("You have", lives, "lives.")
      else:
        lives = 5
        print("You have 5 lives.")
  except ValueError:                                                                                # Runs if the Value given is not an integer
        lives = 5
        print("You have 5 lives.")
  return (size, lives)


# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)        # Creates dictionary from the function

    # print a game introduction
    print("Welcome to the Hangman Game!\n")
    user_answer = "y"
    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while user_answer.upper() == "Y":                       # Creates loop where if user answers "N" to play a new game the game will not run.

      game_options = get_game_options()                     # Creates game options
      len_word = game_options[0]                            # Gets length of the word
      lives = game_options[1]                               # gets amount of lives
      lives_lost = 0                                        # Sets how many lives were lost
      list_of_words = dictionary[len_word]                  # Gets the list of words(value) corrisponding to the length of the word(key)
      word = choice(list_of_words)                          # Randomly chooses word from the list
      word = list(word)                                     # Separates the word into individual letters put into a list
      letters_chosen = []                                   # Creates a list for the letters which the user has guessed
      hidden_word = ["__"] * len_word                       # Creates a list filled with "__" which corrispond to each letter of the word
    
        # START GAME LOOP   (INNER PROGRAM LOOP)
      while 1 == 1:                                                                  # Basic while loop to keep the game running
          letter_index = -1

          print("Letters chosen:", ", ".join(letters_chosen))                       #Prints the basic game menu by making the hidden_word list into a string
          print(" ".join(hidden_word), "lives:", lives, "O" * lives + "X" * lives_lost, "\n") 
        
          if "__" not in hidden_word:
            print("Congratulations!!! You won! The word is", "".join(word), "\n")    # If the user solves the word it will print the winning screen
            break
          elif lives == 0:
            print("You lost! The word is", "".join(word), "\n")                      # If the user is all out of lives the game will print the losing screen
            break
          else:
            while 1 == 1:                                                             # Basic while loop to keep asking for the user's guess until given a letter guess
              user_guess = input("Please choose a new letter > \n")
              user_guess = user_guess.upper()
              if user_guess in letters_chosen:                                        # Runs if given the same number which they have already guessed
                print("\nYou have already chosen this letter.")
              else:
                  if user_guess.isalpha() == True and len(user_guess) == 1:           # Checks that the user's guess was a lewtter and is only one letter
                    letters_chosen.append(user_guess)                                 # Adds the current guessed letter to the list of all chosen letters
                    if user_guess not in word:                                        # Checks to see if the guessed l;etter is actually in the secret word
                      print("\nYou guessed wrong, you lost one life.")
                      lives -= 1                                                      # Changes current lives and lost lives appropriately if letter is not found in the word
                      lives_lost += 1
                    else:
                      print("\nYou guessed right!")                                   # Runs only if the guessed letter is found in the word
                      for i in word:
                        letter_index += 1                                             # Begins a for loop to replace the "__" with the corrent letter in the correct place
                        if user_guess == i:
                          hidden_word[letter_index] = i

                  else:
                    print("\nPlease Try Again.")                                      # Runs if the users' guess was a number or characters more than 1
                    break
                  break

      user_answer = input("Would you like to play again [Y/N]? ")                   # Asks the user if they want to play again 
                                                                                    # which will either start the loop again or stop the loop
    print("\nGoodbye.")                                     # Phase will print when the user                                          
                                                                                    # answers "N" in response to a new game