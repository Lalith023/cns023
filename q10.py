import hashlib

# Function to perform SHA-3 hashing
def sha3_1024(message):  
    message += b'\x06'

    hash_obj = hashlib.sha3_512(message)
    digest = hash_obj.digest()

    return digest

message = b'Hello, world!'
hash_result = sha3_1024(message)
print("SHA-3 hash (1024 bits) of 'Hello, world!':", hash_result.hex())
 
