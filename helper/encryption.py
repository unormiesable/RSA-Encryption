def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, cipher):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plaintext)