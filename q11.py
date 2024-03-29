 import numpy as np
def text_to_numbers(text):
    return [ord(char.lower()) - ord('a') for char in text if char.isalpha()]

def numbers_to_text(numbers):
    return ''.join([chr(num + ord('a')) for num in numbers])

def pad_plaintext(text, n):
    remainder = len(text) % n
    if remainder != 0:
        return text + 'x' * (n - remainder)
    return text
def hill_encrypt(plaintext, key):
    n = len(key)
    plaintext = pad_plaintext(plaintext.replace(" ", ""), n)
    numbers = text_to_numbers(plaintext)
    key_matrix = np.array(key).reshape(n, n)
    ciphertext = ""
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n]).reshape(n, 1)
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext += numbers_to_text(encrypted_block.flatten())
    return ciphertext

def hill_decrypt(ciphertext, key):
    n = len(key)
    key_matrix = np.array(key).reshape(n, n)
    key_matrix_inv = np.linalg.inv(key_matrix)
    det = int(round(np.linalg.det(key_matrix)))
    adjugate = (det * np.linalg.inv(key_matrix)).astype(int) % 26
    numbers = text_to_numbers(ciphertext)
    plaintext = ""
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n]).reshape(n, 1)
        decrypted_block = np.dot(adjugate, block) % 26
        plaintext += numbers_to_text(decrypted_block.flatten())
    return plaintext

plaintext = "meet me at the usual place at ten rather than eight oclock"
key = [9, 4, 5, 7]
ciphertext = hill_encrypt(plaintext, key)
print("Encrypted:", ciphertext)

decrypted_text = hill_decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
