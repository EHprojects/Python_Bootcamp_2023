alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    new_text = []
    for letter in plain_text:
        pos = alphabet.index(letter)
        new_pos = (pos + shift_amount) % 26
        new_text.append(alphabet[new_pos])

    print(f"The enciphered text is: {''.join(new_text)}")


def decrypt(plain_text, shift_amount):
    new_text = []
    for letter in plain_text:
        pos = alphabet.index(letter)
        new_pos = (pos - shift_amount) % 26
        new_text.append(alphabet[new_pos])

    print(f"The enciphered text is: {''.join(new_text)}")


def caesar(cipher_direction, start_text, shift_amount):
    new_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        pos = alphabet.index(letter)
        new_pos = (pos + shift_amount) % 26
        new_text += alphabet[new_pos]

    print(f"The {direction}d text is: {new_text}")


caesar(direction, text, shift)
