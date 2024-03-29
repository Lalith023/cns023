import random

def generate_key_stream(length):
    return [random.randint(0, 26) for _ in range(length)]

def shift_letter(letter, shift):
    ascii_offset = 65 if letter.isupper() else 97
    return chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)

def vigenere_cipher(plaintext, key_stream):
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            ciphertext += shift_letter(plaintext[i], key_stream[i])
        else:
            ciphertext += plaintext[i]
    return ciphertext

# Test the function
plaintext = "Hello, World!"
key_stream = generate_key_stream(len(plaintext))
ciphertext = vigenere_cipher(plaintext, key_stream)

print(f"Plaintext: {plaintext}")
print(f"Key Stream: {key_stream}")
print(f"Ciphertext: {ciphertext}")
