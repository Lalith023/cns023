import random
def monoalphabetic_key():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))
def encrypt(plaintext, key):
    encrypted = ""
    for char in plaintext.lower():
        if char.isalpha():
            encrypted += key[char]
        else:
            encrypted += char
    return encrypted
def decrypt(ciphertext, key):
    inverted_key = {v: k for k, v in key.items()}
    decrypted = ""
    for char in ciphertext.lower():
        if char.isalpha():
            decrypted += inverted_key[char]
        else:
            decrypted += char
    return decrypted
key = monoalphabetic_key()
plaintext = "The quick brown fox jumps over the lazy dog"
encrypted = encrypt(plaintext, key)
decrypted = decrypt(encrypted, key)
print(f"Key: {key}")
print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
