from morse_code_table import CODE
from art import logo
from playsound import playsound


# A text-based Python program to convert Strings into Morse Code.

print(logo)

text = input("Please enter a text to turn into morse code : \n").upper()

morse_code = []

for char in text:
   morse_code.append(CODE[char])


print()
print("*"*100)
print(f"Your text : {text}")

print(*morse_code,sep="\t")
print("*"*100)

for code in morse_code:
   for char in code:
      if (char == '-'):
         playsound('sound/morse_line.mp3')
      elif(char =='.'):
         playsound('sound/morse_dot.mp3')