def caesar_cipher(text, k, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97  #
            if mode == 'encrypt':
                result += chr((ord(char) - shift + k) % 26 + shift)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - k + 26) % 26 + shift)
        else:
            result += char  
    return result

plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = 23  

encrypted_text = caesar_cipher(plaintext, key, 'encrypt')
print(f"Encrypted: {encrypted_text}")

decrypted_text = caesar_cipher(encrypted_text, key, 'decrypt')
print(f"Decrypted: {decrypted_text}")
