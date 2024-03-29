import numpy as np
from sympy import matrix

def format_str(text):
    text = text.upper().replace(" ", "")
    return text

def encrypt(message, key):
    message_vector = [ord(i) - 65 for i in message]
    key_matrix = np.array([[key[i] for i in range(j, j+2)] for j in range(0, len(key), 2)])
    cipher_matrix = np.dot(key_matrix, message_vector) % 26
    cipher_text = ''.join([chr(i + 65) for i in cipher_matrix])
    return cipher_text

def decrypt(cipher_text, key):
    cipher_vector = [ord(i) - 65 for i in cipher_text]
    key_matrix = Matrix([[key[i] for i in range(j, j+2)] for j in range(0, len(key), 2)])
    key_matrix_inv = key_matrix.inv_mod(26)
    message_matrix = np.dot(key_matrix_inv, cipher_vector) % 26
    message_text = ''.join([chr(int(i) + 65) for i in message_matrix])
    return message_text

message = "meetmeattheusualplaceattenratherthaneightoclock"
key = [9, 4, 5, 7]

# Format the message and key
message = format_str(message)

# Make sure the message length is a multiple of 2
if len(message) % 2 != 0:
    message += "X"

# Encrypt the message
cipher_text = ""
for i in range(0, len(message), 2):
    cipher_text += encrypt(message[i:i+2], key)
print("Ciphertext:", cipher_text)

# Decrypt the message
message_text = ""
for i in range(0, len(cipher_text), 2):
    message_text += decrypt(cipher_text[i:i+2], key)
print("Decrypted Text:", message_text)
