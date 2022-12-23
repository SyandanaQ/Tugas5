# Enkripsi
def encrypt(plaintext, a, b):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            if ch.isupper():
                ciphertext += chr((((ord(ch) - 65) * a) + b) % 26 + 65)
            else:
                ciphertext += chr((((ord(ch) - 97) * a) + b) % 26 + 97)
        else:
            ciphertext += ch
    return ciphertext

# Dekripsi
def decrypt(ciphertext, a, b):
    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            if ch.isupper():
                plaintext += chr(((ord(ch) - 65 - b) * a ** -1) % 26 + 65)
            else:
                plaintext += chr(((ord(ch) - 97 - b) * a ** -1) % 26 + 97)
        else:
            plaintext += ch
    return plaintext

# Contoh penggunaan
plaintext = "Syandana Qatrunada"
a = 5
b = 8
ciphertext = encrypt(plaintext, a, b)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypt(ciphertext, a, b))
