def encrypt(plaintext, key):
    # Add filler character to make plaintext length multiple of key length
    filler = len(plaintext) % key
    if filler != 0:
        plaintext += "X" * (key - filler)
    
    # Create the encryption matrix
    matrix = [[' ' for _ in range(key)] for _ in range(len(plaintext) // key)]
    index = 0
    for i in range(len(plaintext) // key):
        for j in range(key):
            matrix[i][j] = plaintext[index]
            index += 1
    
    # Read the matrix in column-wise order to get the encrypted text
    ciphertext = ''
    for j in range(key):
        for i in range(len(plaintext) // key):
            ciphertext += matrix[i][j]
    
    return ciphertext

def decrypt(ciphertext, key):
    # Create the decryption matrix
    matrix = [[' ' for _ in range(key)] for _ in range(len(ciphertext) // key)]
    index = 0
    for j in range(key):
        for i in range(len(ciphertext) // key):
            matrix[i][j] = ciphertext[index]
            index += 1
    
    # Read the matrix in row-wise order to get the decrypted text
    plaintext = ''
    for i in range(len(ciphertext) // key):
        for j in range(key):
            plaintext += matrix[i][j]
    
    return plaintext.strip('X')

def main():
    plaintext = "Hello World"
    key = 4

    # Encryption
    encrypted_text = encrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)

    # Decryption
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()