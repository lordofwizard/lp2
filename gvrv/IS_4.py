from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_aes(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = _pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_aes(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    return _unpad(decrypted_text)

def _pad(plaintext):
    padding_length = AES.block_size - (len(plaintext) % AES.block_size)
    return plaintext + bytes([padding_length] * padding_length)

def _unpad(padded_text):
    padding_length = padded_text[-1]
    return padded_text[:-padding_length]

def main():
    key = get_random_bytes(16)  # 128-bit key
    plaintext = b"Hello, World!"

    # Encryption
    ciphertext = encrypt_aes(key, plaintext)
    print("Encrypted:", ciphertext.hex())

    # Decryption
    decrypted_text = decrypt_aes(key, ciphertext)
    print("Decrypted:", decrypted_text.decode())

if __name__ == "__main__":
    main()