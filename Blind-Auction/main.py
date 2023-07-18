from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program")
d={}
bidders = True
while bidders:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  d[name] = bid
  any_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if any_bidders =="yes":
    clear()
  else:
    bidders =False

maxx= 0
for i in d:
  if d[i] >maxx:
    maxx = d[i]
    winner = i
  
print(f"The winner is {winner} with a bid of {maxx}.")

  
