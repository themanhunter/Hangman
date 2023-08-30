#Importing the random module, the word_list from Hangman_word and logo and stages from Hangman_art
import random
from Hangman_word import word_list
from Hangman_art import logo, stages

#Setting the state of the game
end_of_game = False

#Setting lives
lives = 6

#Displaying the logo from Hangman_art
print(logo)

#Choosing a random word
chosen_word = random.choice(word_list)

#Making the underscore display
display = []
for _ in chosen_word:
    display += "_"
print(display)


#While loop to loop the game until end_of_game is set to true.
while not end_of_game:

    #User input for letter guess
    guess = input("Please choose a letter: ").lower()

    #Checks if they have already guessed a letter.
    if guess in display:
        print(f"You have already guessed {guess}")

    #Check if user input is correct and updates display
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    #Checks if the letter is not in the word, updates lives 
    if guess not in chosen_word:
        lives -= 1
        print(f"No match for {guess}")
        if lives == 0:
            end_of_game = True
            print(f"You lose, the word was {chosen_word}")
            

    #Checks to see if _ is in the display, if not it updates the end_of_game
    if "_" not in display:
        end_of_game = True
        print("You win!")

    #Prints the stages from Hangman_art
    print(stages[lives])

