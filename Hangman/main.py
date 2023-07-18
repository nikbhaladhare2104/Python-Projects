import random
import hangman_art
import hangman_words


print(hangman_art.logo)
#word_list = ["aardvark", "baboon", "camel"]
print("\n")
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"



count = 6

#Check guessed letter
while "_"  in display and count>0:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You have already chosen {guess} . Try differnet one.")
  
  
  if guess in chosen_word:
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
  else:
    count-=1
    print(f"You chose {guess}. Its not in the word. You lose a life.")
    print(hangman_art.stages[count])
      
  print(" ".join(display))
  print("\n")
if "_" not in display:
  print("You won.")
else:
  print("You lose. Game Over.")
