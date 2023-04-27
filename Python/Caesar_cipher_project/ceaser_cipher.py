alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
##########################
def caesar(entered_text, shift_amount, func_direction):
    
    end_text = ""
    if func_direction == "decrypt":
        shift_amount *= -1
    for char in entered_text:
        if char not in alphabet:
            end_text += char
        else:     
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
    print("The result is:\n", end_text)
############################
from art import logo
print(logo)
############################
game_status_end = False
while not game_status_end:
    direction = input("Do you want to decrypt or encrypt a message ? ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(entered_text=text, shift_amount=shift, func_direction=direction)

    restart = input("if you want to reset say 'yes', else say 'no'\n").lower()
    if restart == "no":
        game_status_end = True
        print("Goodbye!")
