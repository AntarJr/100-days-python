
logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP""'""'"   `"Y8ba, ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
           88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift_amount):
    result_word = "" 
    original_text = text
    for letter in original_text:
        if letter in alphabet:
            placment = alphabet.index(letter)
            new_placment = (shift_amount + placment) % 26
            new_letter = alphabet[new_placment]
            result_word += new_letter
        else: 
            result_word += letter
    print(f"your new word is {result_word}")

print(logo)
valid_direction = ["encode" , "decode"]
while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in valid_direction :
        print("choose a valid option")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        shift_amount = shift
    elif direction == "decode":
        shift_amount = -shift

    caesar(text, shift_amount)

    while True:
        rerun = input("Do you want to run the program again?\n").lower().strip()

        if rerun == "yes":
            break

        elif rerun == "no":
            print("Thank you for trying our Cipher program")
            exit()

        else:
            print("Kindly choose a valid answer")
