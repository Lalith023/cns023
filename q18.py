def diffie_hellman(a, q, xA, xB):
    # Alice computes and sends A = a^xA mod q
    A = pow(a, xA, q)

    # Bob computes and sends B = a^xB mod q
    B = pow(a, xB, q)

    # Alice computes the shared secret key = B^xA mod q
    keyA = pow(B, xA, q)

    # Bob computes the shared secret key = A^xB mod q
    keyB = pow(A, xB, q)

    return keyA, keyB

# Test the function
a = 5
q = 23
xA = 6
xB = 15
keyA, keyB = diffie_hellman(a, q, xA, xB)

print(f"Shared secret key computed by Alice: {keyA}")
print(f"Shared secret key computed by Bob: {keyB}")
