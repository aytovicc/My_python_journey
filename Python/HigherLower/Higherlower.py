# ART VE DATA EKLENMELİ
#from game_data import data
#from art import logo, vs
#from replit import clear
import random

print(logo)

def random_account():
  return random.choice(data)

  
def account_information(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, {description}, {country}"
 

def compare(guess, account_A, account_B):
  A_score = account_A["follower_count"]
  B_score = account_B["follower_count"]
  winner = 0
  if A_score > B_score:
    winner = "a"
  if B_score > A_score:
    winner = "b"

  if guess == winner:
    return True
  else:
    return False


def game(A, B):
  
  print("A:",account_information(A))
  print(vs)
  print("B:",account_information(B))
  
  guess = input("Which one has higher follower's on instagram? ").lower()
  return guess

A = random_account()
B = random_account()

point = 0
game_status = False
while not game_status:
  
  go = True
  while go:  
    clear()
    A = B
    B = random_account()
    if A == B:
      B = random_account()
    
    guess = (game(A, B))
    result = compare(guess, A, B)
    if result == True:
      point += 1
    else:
      go = False
      game_status = True
      
print(f"\nYour score is {point}. Game ended!")