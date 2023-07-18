rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

l = random.randint(0,2)
r=""
if l ==0:
  r = rock
elif l == 1:
  r = paper
else:
  r= scissors

i1=""
i = input("What do you choose? Rock, Paper or Scissors?\n")
if i =="Rock":
  i1 = rock
elif i == "Paper":
  i1 = paper
elif i == "Scissors":
  i1= scissors

print("You chose:")
print(i1)
print(f"Computer chose: {r} ")

if i1 == rock:
  if r == paper:
    print("You Lose.")
  elif r == scissors:
    print( " You Win.")
  else:
    print("You chose the same option. Try again.")
elif i1 == paper:
  if r == scissors:
    print("You Lose.")
  elif r == rock:
    print( " You Win.")
  else:
    print("You chose the same option. Try again.")
else:
  if r == paper:
    print("You Win.")
  elif r == rock:
    print( " You Lose.")
  else:
    print("You chose the same option. Try again.")
    
  
