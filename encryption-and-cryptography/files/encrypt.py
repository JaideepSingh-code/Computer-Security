import base64
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# 1. Your full name as required
plaintext = "Jaideep Singh"

# 2. AES-256 requires a 32-byte key
key = os.urandom(32)  # secure random key
iv = os.urandom(16)   # 16-byte IV for CBC mode

# 3. Padding plaintext using PKCS#7
padder = padding.PKCS7(128).padder()  # 128-bit block size
padded_plaintext = padder.update(plaintext.encode()) + padder.finalize()

# 4. Encrypt using AES-256 CBC
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

# 5. Encode encrypted value in BASE64
ciphertext_b64 = base64.b64encode(iv + ciphertext).decode()

# 6. Decrypt the ciphertext to get the original string
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

# 7. Remove padding
unpadder = padding.PKCS7(128).unpadder()
decrypted_text = unpadder.update(decrypted_padded) + unpadder.finalize()

# 8. Print required outputs
print(plaintext)               # Original plaintext
print(ciphertext_b64)         # Encrypted (BASE64)
print(decrypted_text.decode())# Decrypted plaintext (should match original)

# 9. Write the same outputs to output.txt
with open("output.txt", "w") as f:
    f.write(plaintext + "\n")
    f.write(ciphertext_b64 + "\n")
    f.write(decrypted_text.decode() + "\n")