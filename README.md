# Computer Security

A collection of security research and practical exercises covering six core areas of computer security — from cryptographic implementations to malware analysis — using industry-standard tools and methodologies.

## Overview

This repository documents hands-on work across offensive and defensive security domains, including vulnerability exploitation, network defense, and forensic analysis. Each module contains detailed methodology documentation, tool configurations, and findings.

## Modules

| Module | Focus Area | Key Tools |
|--------|-----------|-----------|
| [Encryption and Cryptography](./encryption-and-cryptography) | AES/RSA implementation, digital signatures, custom Python encryption client | OpenSSL, Python `cryptography` |
| [Linux Security and Social Engineering](./linux-security-and-social-engineering) | CLI security challenges, browser exploitation, phishing attack vectors | OverTheWire Bandit, BeEF Framework |
| [Password Security Analysis](./password-security-analysis) | Offline hash cracking, online brute-force, dictionary attacks | John the Ripper, Hydra, rockyou.txt |
| [Penetration Testing](./penetration-testing) | Network reconnaissance, CVE exploitation, reverse shells | Nmap, Metasploit Framework |
| [Malware Analysis and Intrusion Detection](./malware-analysis-and-ids) | Static analysis, YARA rule development, Snort IDS deployment | YARA, Snort 3, exiftool, binwalk |
| [Web Application Security](./web-application-security) | XSS (stored/reflected/upload), CSRF exploitation and defense | Google Gruyere, custom payloads |

## Tech Stack

**Offensive Tools:** Metasploit, Nmap, Hydra, John the Ripper, BeEF, Burp Suite

**Defensive Tools:** Snort IDS, YARA, OpenSSL

**Analysis Tools:** exiftool, binwalk, strings, sha256sum

**Languages:** Python, Bash, HTML/JavaScript

**Environment:** Kali Linux, Metasploitable3

## Highlights

- **Real malware analysis** — analyzed an AgentTesla infostealer sample from MalwareBazaar, including metadata forensics and custom YARA detection rules
- **CVE exploitation** — demonstrated exploitation of CVE-2015-3306 (ProFTPD mod_copy) and CVE-2010-2075 (UnrealIRCd backdoor) with full attack chain documentation
- **Custom tooling** — built a Python AES-256-CBC encryption client from scratch using the `cryptography` library's hazmat primitives
- **IDS rule development** — deployed Snort 3 with custom detection rules, including analysis of HTTPS limitations on signature-based detection
- **Web attack vectors** — demonstrated 4 distinct attack types (File Upload XSS, Reflected XSS, Stored XSS, CSRF) with root cause analysis and countermeasures

## Project Structure

```
Computer-Security/
├── encryption-and-cryptography/
│   ├── files/
│   │   ├── encrypt.py                  # Custom AES-256-CBC encryption client
│   │   ├── plaintext.txt               # Sample plaintext input
│   │   ├── encrypted_file.enc          # AES-encrypted output
│   │   ├── decrypted_file.txt          # Decrypted verification
│   │   ├── symmetric_key.key           # AES symmetric key
│   │   ├── public_key.pem              # RSA public key
│   │   ├── private_key.pem             # RSA private key
│   │   ├── rsa_encrypted.enc           # RSA-encrypted data
│   │   ├── rsa_decrypted.txt           # RSA-decrypted output
│   │   ├── signature.bin               # Digital signature
│   │   └── output.txt                  # Execution output
│   ├── README.md
│   ├── Solutions.pdf
│   └── Task.pdf
├── linux-security-and-social-engineering/
│   ├── README.md, Solutions.pdf, Task.pdf
├── password-security-analysis/
│   ├── README.md, Solutions.pdf, Task.pdf
├── penetration-testing/
│   ├── README.md, Solutions.pdf, Task.pdf
├── malware-analysis-and-ids/
│   ├── README.md, Solutions.pdf, Task.pdf
├── web-application-security/
│   ├── README.md, Solutions.pdf, Task.pdf
└── README.md
```

## Disclaimer

All security testing was performed in controlled, authorized environments (local VMs, intentionally vulnerable applications). This repository is for educational and portfolio purposes only.
