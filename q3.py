from itertools import product
def generate_playfair_key(keyword):
    keyword_no_duplicates = "".join(sorted(set(keyword), key=keyword.index))
    matrix = [[None for _ in range(5)] for _ in range(5)]
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    used = set(keyword_no_duplicates)
    for i, letter in enumerate(keyword_no_duplicates.upper()):
        matrix[i // 5][i % 5] = letter
    for letter in alphabet:
        if letter not in used:
            i += 1
            matrix[i // 5][i % 5] = letter
            used.add(letter)
    return matrix
def playfair_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace("J", "I")
    digraphs = []
    i = 0
    while i < len(plaintext):
        digraph = plaintext[i]
        i += 1
        if i < len(plaintext) and plaintext[i] != digraph:
            digraph += plaintext[i]
            i += 1
        else:
            digraph += 'X'
        digraphs.append(digraph)
    ciphertext = ""
    for digraph in digraphs:
        pos = [None, None, None, None]
        for i, j in product(range(5), repeat=2):
            if key_matrix[i][j] == digraph[0]:
                pos[0], pos[1] = i, j
            elif key_matrix[i][j] == digraph[1]:
                pos[2], pos[3] = i, j
        if pos[0] == pos[2]: 
            ciphertext += key_matrix[pos[0]][(pos[1] + 1) % 5]
            ciphertext += key_matrix[pos[2]][(pos[3] + 1) % 5]
        elif pos[1] == pos[3]:
            ciphertext += key_matrix[(pos[0] + 1) % 5][pos[1]]
            ciphertext += key_matrix[(pos[2] + 1) % 5][pos[3]]
        else:  
            ciphertext += key_matrix[pos[0]][pos[3]]
            ciphertext += key_matrix[pos[2]][pos[1]]

    return ciphertext
keyword = "MONARCHY"
key_matrix = generate_playfair_key(keyword)
plaintext = "INSTRUMENTS"
encrypted = playfair_encrypt(plaintext, key_matrix)
print(f"Key Matrix: {key_matrix}")
print(f"Encrypted: {encrypted}")
