from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_CBC_3DES(plain_text, key):
    cipher = DES3.new(key, DES3.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text, DES3.block_size))
    return cipher.iv, cipher_text

def decrypt_CBC_3DES(cipher_text, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
    plain_text = unpad(cipher.decrypt(cipher_text), DES3.block_size)
    return plain_text

# Test the function
key = get_random_bytes(24) # 3DES requires a 24-byte key
plain_text = b"Hello, World!"

iv, cipher_text = encrypt_CBC_3DES(plain_text, key)
print(f"Ciphertext: {cipher_text.hex()}")

decrypted_text = decrypt_CBC_3DES(cipher_text, key, iv)
print(f"Decrypted text: {decrypted_text.decode()}")
