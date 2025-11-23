alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)
game_over = False
def caeserCipher(text, shift, direction):
    output_text = ""
    if direction == 'decode':
        shift *= -1
    for letters in text:
        if letters not in alphabet:
            output_text += letters
        else:
            shifted_position = alphabet.index(letters) + shift
            shifted_position = shifted_position % 26
            output_text += alphabet[shifted_position]
    print(f"Here is the {direction} message {output_text}")

while game_over == False:

    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeserCipher(text, shift, direction)

    playMore = input("Do you want to play again? (type 'y' or 'n')\n").lower()

    if playMore == 'y':
        game_over = False
    elif playMore == 'n':
        game_over = True




