from art import logo, vs
from game_data import data
import os
import random


print(logo)

# clear function
def clear():
    os.system("clear")

def random_account():
  # Get the random account from the data
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return (f"{name}, a {description}, from {country}")

def check_answer(guess, a_followers, b_followers):
   if a_followers > b_followers:
      return guess == "a"
   else:
      return guess == "b"
   
score = 0
game_finished = False

a_account = random_account()
b_account = random_account()

while not game_finished:
  a_account = b_account
  b_account = random_account()
  while a_account == b_account:
     b_account = random_account()
  
  print(f"Compare A: {format_data(a_account)}")
  print(vs)
  print(f"Compare B: {format_data(b_account)}")

  guess = input("Who has more insta followers?: ")

  if check_answer(guess, a_account["follower_count"], b_account["follower_count"]):
    clear()
    score+=1
    print(logo)

    print(f"You are right. Current score: {score}")
  else:
    clear()
    print(logo)

    print(f"Sorry. That's wrong. Final score: {score}")
    game_finished = True

  
  