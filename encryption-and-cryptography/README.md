# Encryption and Cryptography

Hands-on exploration of symmetric and asymmetric cryptographic systems, covering key generation, encryption/decryption workflows, digital signatures, and a custom Python encryption client.

## Objective

Implement and compare AES (symmetric) and RSA (asymmetric) encryption schemes using OpenSSL, analyze the performance implications of different key sizes, create and verify digital signatures, and build a Python application that performs AES-256-CBC encryption from scratch.

## Tools and Technologies

- **OpenSSL** — command-line cryptographic toolkit
- **Python 3** with `cryptography` library (hazmat primitives)
- **AES-256-CBC** — symmetric block cipher
- **RSA-2048** — asymmetric key pair encryption
- **SHA-256** — cryptographic hash function for digital signatures
- **Kali Linux** — operating environment

## Methodology

### Part 1: Symmetric Encryption (AES)

Generated a 256-bit random symmetric key and used it to encrypt/decrypt a plaintext file through AES-256-CBC with salt:

```bash
# Generate 256-bit key
openssl rand -base64 32 > symmetric_key.key

# Encrypt with AES-256-CBC
openssl enc -aes-256-cbc -salt -in plaintext.txt -out encrypted_file.enc -pass file:symmetric_key.key

# Decrypt
openssl enc -d -aes-256-cbc -in encrypted_file.enc -out decrypted_file.txt -pass file:symmetric_key.key

# Verify integrity
diff plaintext.txt decrypted_file.txt
```

Benchmarked encryption performance across key sizes (128, 192, 256-bit) using the `time` command to measure computational overhead per AES round count (10, 12, 14 rounds respectively).

### Part 2: Asymmetric Encryption (RSA)

Generated a 2048-bit RSA key pair, encrypted data with the public key, and decrypted with the private key:

```bash
# Generate RSA key pair
openssl genrsa -out private_key.pem 2048
openssl rsa -pubout -in private_key.pem -out public_key.pem

# Digital signature (sign + verify)
openssl dgst -sha256 -sign private_key.pem -out signature.bin plaintext.txt
openssl dgst -sha256 -verify public_key.pem -signature signature.bin plaintext.txt
```

### Part 3: Python Encryption Client

Built a Python application (`encrypt.py`) that:
- Generates a secure random 32-byte key and 16-byte IV
- Applies PKCS#7 padding to plaintext
- Encrypts using AES-256-CBC via the `cryptography` library's hazmat primitives
- Encodes ciphertext to Base64 (IV prepended) for safe transport
- Decrypts and verifies round-trip integrity

## Key Findings

- **Salt prevents rainbow table attacks** — the `-salt` flag ensures identical plaintext/password combinations produce different ciphertexts every time
- **Wrong-key decryption fails silently** — produces unreadable garbage rather than throwing an error, highlighting the importance of key management
- **Key size vs. performance** — AES-256 requires 14 rounds vs. AES-128's 10 rounds, but the performance difference is negligible for typical file sizes
- **RSA is significantly slower than AES** — due to modular exponentiation with large primes; hybrid encryption (RSA for key exchange, AES for data) is the practical standard
- **Digital signatures use hashing for efficiency** — SHA-256 creates a fixed-size digest, ensuring any tampering changes the hash and making verification computationally feasible

## Files

| File | Description |
|------|-------------|
| `files/encrypt.py` | Python AES-256-CBC encryption/decryption client |
| `files/symmetric_key.key` | Generated 256-bit symmetric key |
| `files/private_key.pem` | RSA-2048 private key |
| `files/public_key.pem` | RSA-2048 public key |
| `files/encrypted_file.enc` | AES-encrypted ciphertext |
| `files/decrypted_file.txt` | Decrypted output (matches original) |
| `files/rsa_encrypted.enc` | RSA-encrypted ciphertext |
| `files/signature.bin` | SHA-256 digital signature |
| `files/plaintext.txt` | Original plaintext input |
| `files/output.txt` | Python client output log |
