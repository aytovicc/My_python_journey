import os
from hammer_art import logo
print(logo)

bidders = {}

def adding_to_list(name, amount):
    bidders[name] = f"{amount}"

def clear_display():
    os.system('cls')
    print(logo)
  
bid_status_end = False

while not bid_status_end:

    bidders_name = input("What's your name?\n")
    bid_amount = input("How much you want to pay?\n")

    adding_to_list(name=bidders_name, amount=bid_amount)

    next_bid = input("Will there be another bidder? 'yes' or 'no'\n").lower()

    if next_bid == "yes":
        clear_display()
    elif next_bid == "no":
        bid_status_end = True
        max_value = max(bidders.values())
        who_won = []
        for bidder in bidders:
            if (bidders.get(f"{bidder}")) == max_value:
                who_won.append(bidder)
        else:
            pass    

print(f"{who_won[0]} won this bidding auction by bidding {max_value}$.")    
