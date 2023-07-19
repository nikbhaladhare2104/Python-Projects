# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
d = {row.letter: row.code for index, row in data.iterrows()}

name = input("Enter a word: ").upper()

# name = [i.upper() for i in n]
res = [d[i] for i in name]

print(res)


