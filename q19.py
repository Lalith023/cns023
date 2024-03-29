def generate_subkeys(key):
    # Constants for 128-bit block size
    const_zero = 0x00
    const_rb = 0x87

    # Left shift function
    def left_shift(k):
        return ((k << 1) & 0xFFFFFFFE) ^ ((k >> 7) * const_rb)

    # Generate the first subkey
    k1 = left_shift(key)
    if key & 0x80:
        k1 ^= const_rb

    # Generate the second subkey
    k2 = left_shift(k1)
    if k1 & 0x80:
        k2 ^= const_rb

    return k1, k2

# Test the function
key = 0x2b7e151628aed2a6abf7158809cf4f3c
k1, k2 = generate_subkeys(key)

print(f"First subkey: {hex(k1)}")
print(f"Second subkey: {hex(k2)}")
