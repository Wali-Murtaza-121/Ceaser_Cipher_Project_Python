alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

def caeser(direction,text,shift):
    end_of_game = False
    while not end_of_game:
        result_text = ""
        if direction == "decode":
            shift = shift * -1
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift
                result_text += alphabet[new_position]
            else:
                result_text += letter
        print(f"Here are the {direction}d result: {result_text}")
        user_choice = input("Type 'yes' to go again. Otherwise 'No'\n").lower()
        if user_choice == "no":
            end_of_game = True
            print("Goodbye")
        else:
            end_of_game = False
            direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt: ").lower()
            text = input("Type message: ").lower()
            shift = int(input("Type Number to shift the number: "))
            
direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt: ").lower()
text = input("Type message: ").lower()
shift = int(input("Type Number to shift the number: "))
caeser(direction,text,shift)