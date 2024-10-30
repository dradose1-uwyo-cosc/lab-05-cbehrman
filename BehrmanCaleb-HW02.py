# Caleb Behrman
# UWYO COSC 1010
# 10/29/24
# HW 02
# Lab Section: 15
# Sources, people worked with, help given to: I had to ask chatgpt how to do the double spaces and how that works with morsecode

# alright well this assignment seems difficult, here goes the next couple hours of my life hahaha

def main():
    #A long *** dictionary
    morse_code_dict ={
        'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.', 
        'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',   'J': '.---',
        'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',   'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
        'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
        'Z': '--..'
    }

    #Get the person to say something
    input_string=input("Enter a string: ")

    #Empty list for Morse code output
    morse_output=[]

    #Process each letter in the input string
    for char in input_string:
        if char.isalpha():  #This basically just checks to see if its an actual letter
            morse_char=morse_code_dict[char.upper()]
            morse_output.append(morse_char)  #This just adds a Morse code character to the outpiut
        elif char == ' ':
            morse_output.append('')  #The space

    #This just adds a space
    morse_code = ' '.join(morse_output).replace('  ', '    ')  
#Replace placeholders with double spaces

    print(morse_code)

if __name__ == "__main__":
    main() #This just makes sure its being run directly and calls the main function thingy up top