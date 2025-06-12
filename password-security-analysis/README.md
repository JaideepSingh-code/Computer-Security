# Password Security Analysis

Offline and online password cracking using John the Ripper and Hydra, demonstrating the vulnerability of weak passwords to dictionary and brute-force attacks.

## Objective

Perform offline hash cracking with John the Ripper against extracted `/etc/shadow` hashes and online brute-force attacks with Hydra against a live SSH service. Compare attack methodologies, analyze the effectiveness of dictionary-based approaches using the `rockyou.txt` wordlist, and evaluate GPU-accelerated alternatives.

## Tools and Technologies

- **John the Ripper 1.9.0-jumbo** — offline password hash cracker
- **Hydra** — online network service brute-force tool
- **rockyou.txt** — 14M+ entry wordlist from the 2009 RockYou breach
- **SSH** — target network service
- **Kali Linux** — operating environment

## Methodology

### Part 1: Offline Cracking with John the Ripper

Extracted the password hash from `/etc/shadow` and ran three attack modes:

```bash
# Extract target hash
sudo grep test /etc/shadow > hash.txt

# Default cracking mode (auto-detect failed — required explicit format)
john --format=crypt hash.txt

# Dictionary attack with rockyou.txt
john --wordlist=/usr/share/wordlists/rockyou.txt --format=crypt hash.txt

# Filtered dictionary attack (4-6 character passwords only)
john --wordlist=/usr/share/wordlists/rockyou.txt --min-length=4 --max-length=6 --format=crypt hash.txt

# Verify cracked passwords
john --format=crypt hash.txt --show
```

**Issue encountered:** The initial run without `--format=crypt` returned "No password hashes loaded" because JtR could not auto-detect the hash format from the shadow file. Specifying the format explicitly resolved this.

### Part 2: Online Brute-Force with Hydra

Targeted a live SSH service on the local network:

```bash
# Identify target IP
ifconfig | grep -A 8 eth0    # -> 10.0.2.4

# Run Hydra against SSH
hydra -l test -p password.lst 10.0.2.4 -t 4 ssh
```

**Parameters:** `-l test` (username), `-p password.lst` (password file), `-t 4` (4 parallel threads), `ssh` (target protocol).

**Result:** `[22][ssh] host: 10.0.2.4 login: test password: test` — cracked in under one second.

### Part 3: Alternative Tools Research

Evaluated **Hashcat** as a GPU-accelerated alternative to John the Ripper. Hashcat leverages GPU parallelism for dramatically faster hash computation, supports 300+ hash types natively, and is particularly effective against computationally expensive hash functions (bcrypt, scrypt, Argon2) where CPU-based tools bottleneck.

## Key Findings

- **Weak passwords are trivially crackable** — the password "test" was cracked instantly by both tools
- **Offline vs. online attack trade-offs** — JtR operates against extracted hash files (no network noise, unlimited attempts) while Hydra attacks live services (network-visible, rate-limitable, lockout-prone)
- **Hash format detection matters** — JtR's auto-detection can fail on modern shadow file formats; always verify with `--format`
- **rockyou.txt remains devastatingly effective** — with 14M+ real-world passwords, dictionary attacks succeed against the majority of human-chosen passwords
- **Defense recommendations** — enforce minimum 12+ character passwords, implement account lockout policies, use bcrypt/Argon2 for hashing, and deploy fail2ban for SSH protection
