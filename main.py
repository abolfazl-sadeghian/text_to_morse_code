from morse_code_table import CODE
from art import logo
from playsound import playsound

# A text-based Python program to convert Strings into Morse Code.

print(logo)

text = input("Please enter a text to turn into morse code : \n").upper().split(' ')

morse_code = []


def word_to_morse_code(word: str):
    for char in word:
        morse_code.append(CODE[char])
    morse_code.append('|')

for item in text:
    word_to_morse_code(item)

print()
print("*" * 100)
print("Your text :\t",*text, sep=" ")

print("Morse Code :\t", *morse_code, sep="   ")
print("*" * 100)

for code in morse_code:
    for char in code:
        if (char == '-'):
            playsound('sound/morse_line.mp3')
        elif (char == '.'):
            playsound('sound/morse_dot.mp3')
        elif(char == '|'):
            continue

