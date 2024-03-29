import string
from fractions import gcd

def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and 26 are not coprime. Choose a different value of a.")
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((a * (ord(char) - offset) + b) % 26 + offset)
        else:
            result += char
    return result

def multiplicative_inverse(a):
    for i in range(26):
        if (a * i) % 26 == 1:
            return i
    return 1

def affine_decrypt(text, a, b):
    a_inv = multiplicative_inverse(a)
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((a_inv * (ord(char) - offset - b)) % 26 + offset)
        else:
            result += char
    return result

# Test the functions
a = 7
b = 3
text = "Hello, World!"
encrypted = affine_encrypt(text, a, b)
decrypted = affine_decrypt(encrypted, a, b)

print(f"Original text: {text}")
print(f"Encrypted text: {encrypted}")
print(f"Decrypted text: {decrypted}")
