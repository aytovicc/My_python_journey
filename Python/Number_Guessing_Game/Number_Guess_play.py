from guess_num_art import logo
import random

print(logo)
print("Hey! Welcome to number guess game!")
level = input("Choose a level to play 'hard' or 'easy'?\n").lower()

secret_number = random.choice(range(1,101))
end_status = False

def difficulty(level):
    if level == "easy":
        return 10
    if level == "hard":
        return 5

def game(number):
    guess = int(input("Make a guess:\n"))
    
    global end_status

    if guess > number:
        return print("----> Too High <----")

    if guess < number:
        return print("----> Too Low <----")

    if guess == number:
        end_status = True
        return print(f"YOU WON!\nThe number was: {number}")
        
        
life = difficulty(level)
print("There you go.")

while not end_status:
    print("")
    print(f"Remaining life: {life}")
    game(secret_number)
    life -= 1

    if life == 0:
        end_status = True
        print(f"SORRY YOU LOSE!\nYou ran out of chance. The number was: {secret_number}")