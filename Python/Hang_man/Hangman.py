import random
from hangman_words import word_list
from hangman_art import*

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
length = 0
##########
display = []
############
for _ in range(word_length):
    display += "_"
    length += 1
print(display)
print("Mysterious word has", str(length) ,"letter(s)")

already_guessed = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in already_guessed:  
      print("!!!!!You already guessed this letter!!!!! -----> ", guess)
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
      #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
          already_guessed.append(guess)
          display[position] = letter
        
    
    
          
    #Check if user is wrong.
    if guess not in chosen_word:
        print("!!!!!This letter is not in the chosen word!!!! -----> ", guess)
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(stages[lives])