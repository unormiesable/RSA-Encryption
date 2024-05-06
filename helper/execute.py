from calculation import generate_keypair
from encryption import encrypt, decrypt

if __name__ == '__main__':
    p = 61
    q = 2
    public_key, private_key = generate_keypair(p, q)
    print("Public key:", public_key)
    print("Private key:", private_key)
    
    message = "Hello, RSA!"
    print("Original message:", message)
    
    encrypted_message = encrypt(public_key, message)
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)
