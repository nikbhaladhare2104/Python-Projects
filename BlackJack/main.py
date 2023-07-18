############### Blackjack Project #####################
import art
import random
from replit import clear
############### Our Blackjack House Rules #####################

def blackjack():
  print(art.logo)
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  f = random.choice(cards)
  s = random.choice(cards)
  comp_f = random.choice(cards)

  # Computer hands
  
  def computer_hand():
    c_h = [comp_f]
    summ = comp_f
    while summ <17:
      com = random.choice(cards)
      c_h.append(com)
      summ+=com
    return c_h
    
  # computer_hand()
  
  c_h = computer_hand()
  
  curr = f+s
  your_cards = [f,s]
  
  while curr <22:
    print(f"      Your cards: {your_cards}, current score : {curr}")
    print(f"      Computer's first card: {comp_f}")
    i1 = input("Type 'y' to get another card, type 'n' to pass: ")
    if i1=="y":
      n_n = random.choice(cards)
      curr = curr + n_n
      your_cards.append(n_n)
    else:
      if sum(c_h) >21:
        print(f"      Your final hand: {your_cards}, Final score: {curr} ")
        print(f"      Computer's final hand: {c_h}, final score: {sum(c_h)}")
        print("Computer went over. You win.")
      elif curr > sum(c_h):
        print(f"      Your final hand: {your_cards}, Final score: {curr} ")
        print(f"      Computer's final hand: {c_h}, final score: {sum(c_h)}")
        print("You win.")
      elif curr == sum(c_h):
        print(f"      Your final hand: {your_cards}, Final score: {curr} ")
        print(f"      Computer's final hand: {c_h}, final score: {sum(c_h)}")
        print("Draw")
      else:
        print(f"      Your final hand: {your_cards}, Final score: {curr} ")
        print(f"      Computer's final hand: {c_h}, final score: {sum(c_h)}")
        print("You lose.")
      curr = 40
        
  
  if curr >21 and curr <40:
    print(f"      Your final hand: {your_cards}, Final score: {curr} ")
    print(f"      Computer's final hand: {c_h}, final score: {sum(c_h)}")
    print("You went over. You lose.")
  

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") =="y":
# if in1 =="y":
  clear()
  blackjack()

