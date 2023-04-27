import os
import random
from black_jack_art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)    

def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "Both went ove. You lost"
    if player_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif player_score == 0:
        return "Won with Blackjack!"
    elif player_score > 21:
        return "You went over, lose!"
    elif computer_score > 21:
        return "Opponent went over, you won!"             
    elif player_score > computer_score:
        return "You won!"
    else:
        return "You lose!"    

def Blackjack():
    
    print(logo)

    players_card = []
    computers_card = []
    is_game_over = False

    for x in range(2):
        players_card.append(deal_card())
        computers_card.append(deal_card())

    player_score = calculate_score(players_card)
    computer_score = calculate_score(computers_card)

    while not is_game_over:

        player_score = calculate_score(players_card)
        computer_score = calculate_score(computers_card)
        print(f"Your cards: {players_card}, Current score: {player_score}")
        print(f"Computers first card: {computers_card[0]}")                

        if player_score == 0 or computer_score == 0 or player_score > 21:
            # 0 DEDİK ÇÜNKÜ FONKSİYONDA 21 GELİRSE 0 DÖNDÜRMESİNİ İSTEDİK.
            is_game_over = True
        else:
            resume = input("Type 'yes' to get another card, type 'no' to pass:\n")    
            if resume == "yes":
                players_card.append(deal_card())
            else:
                is_game_over = True    

    while computer_score != 0 and computer_score < 17:
        computers_card.append(deal_card())
        computer_score = calculate_score(computers_card)            

    
    print(f"Your final hand is: {players_card}. Your score is: {player_score}")
    print(f"Computers final hand is: {computers_card}. Opponents score is: {computer_score}")
    print(compare(player_score, computer_score))

#again = input("Do you want to play again? yes or no?\n")

while input("Do you want to play Blackjack? yes or no?\n") == "yes":
    os.system('cls')
    Blackjack()