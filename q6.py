def matrix(key):
    matrix = []
    for e in key.upper():
        if e not in matrix:
            matrix.append(e)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    for e in alphabet:
        if e not in matrix:
            matrix.append(e)
    
    matrix_group = []
    for e in range(5):
        matrix_group.append('')
    
    matrix_group[0] = matrix[0:5]
    matrix_group[1] = matrix[5:10]
    matrix_group[2] = matrix[10:15]
    matrix_group[3] = matrix[15:20]
    matrix_group[4] = matrix[20:25]
    return matrix_group

def message_to_digraphs(message_original):
    message = []
    for e in message_original:
        message.append(e)
    
    for unused in range(len(message)):
        if " " in message:
            message.remove(" ")
    
    i = 0
    for e in range(len(message)//2):  # Change here
        if message[i] == message[i+1]:
            message.insert(i+1,'X')
        i = i+2
    
    if len(message) % 2 == 1:
        message.append("X")
    
    i = 0
    new = []
    for x in range(1,len(message)//2 + 1):  # Change here
        new.append(message[i:i+2])
        i = i+2
    return new

def find_position(key_matrix, letter):
    x = y = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                x = i
                y = j
    return x, y

def encrypt(message):
    message = message_to_digraphs(message)
    key = "MFHIKUNOPQZVWXYELARGDSTBC"
    key = matrix(key)
    cipher = []
    for e in message:
        p1, q1 = find_position(key, e[0])
        p2, q2 = find_position(key, e[1])
        if p1 == p2:
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            cipher.append(key[p1][q1+1])
            cipher.append(key[p1][q2+1])        
        elif q1 == q2:
            if p1 == 4:
                p1 = -1;
            if p2 == 4:
                p2 = -1;
            cipher.append(key[p1+1][q1])
            cipher.append(key[p2+1][q2])
        else:
            cipher.append(key[p1][q2])
            cipher.append(key[p2][q1])
    return "".join(cipher)

def main():
    message = "Must see you over Cadogan West. Coming at once."
    message = message.upper()
    cipher = encrypt(message)
    print("Encrypted message: ", cipher)

if __name__ == '__main__':
    main()
