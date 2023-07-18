alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
# FOR ENCRYPT
def caesar(direction, text, shift ):
  def encrypt(text , shift):
    l =[]
    for i in range(len(text)):
      id = alphabet.index(text[i])
      if id+shift >25:
        p = id +shift - 26
      else:
        p = id +shift
      l.append(alphabet[p])
    return "".join(l)
    #print("".join(l))


  def decrypt(text , shift):
    l =[]
    for i in range(len(text)):
      id = alphabet.index(text[i])
      if id-shift <0:
        p = id -shift + 26
      else:
        p = id -shift
      l.append(alphabet[p])
      
    return "".join(l)
    #print("".join(l))
    
  if direction == "encode":
    res  = encrypt(text , shift)
  else:
    res = decrypt(text , shift)
  return res
  
#again_1 = True

print(art.logo)
flag = True

while flag:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%26
  
  print(caesar(direction, text, shift))
  
  restart  = input("Type 'y' if you want to go again. Otherwise type 'n'.\n")
  
  if restart =="n":
    flag = False



