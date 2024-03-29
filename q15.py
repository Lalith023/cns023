import string
from collections import Counter

# English letter frequencies
english_freqs = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
    'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
    'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
    'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
    'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
    'y': 0.01974, 'z': 0.00074
}

def shift_letter(letter, shift):
    ascii_offset = 65 if letter.isupper() else 97
    return chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)

def additive_cipher_decrypt(ciphertext, shift):
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            plaintext += shift_letter(letter, -shift)
        else:
            plaintext += letter
    return plaintext

def letter_frequency_attack(ciphertext, top_n):
    letter_counts = Counter(c.lower() for c in ciphertext if c.isalpha())
    total_letters = sum(letter_counts.values())

    plaintexts = []
    for shift in range(26):
        plaintext = additive_cipher_decrypt(ciphertext, shift)
        freqs = {char: count / total_letters for char, count in Counter(plaintext).items()}
        correlation = sum(freqs.get(char, 0) * english_freqs.get(char, 0) for char in string.ascii_lowercase)
        plaintexts.append((correlation, plaintext))

    plaintexts.sort(reverse=True)
    return [text for _, text in plaintexts[:top_n]]

# Test the function
ciphertext = "KHOOR, ZRUOG!"
top_n = 10
possible_plaintexts = letter_frequency_attack(ciphertext, top_n)

print(f"Ciphertext: {ciphertext}")
print(f"Top {top_n} possible plaintexts:")
for i, plaintext in enumerate(possible_plaintexts, 1):
    print(f"{i}. {plaintext}")
