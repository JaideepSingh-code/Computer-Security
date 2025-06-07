# Linux Security and Social Engineering

Progressive Linux command-line security challenges (OverTheWire Bandit) combined with browser-based social engineering attack demonstrations using the BeEF XSS Framework.

## Objective

Develop practical Linux command-line skills through 13 levels of the OverTheWire Bandit wargame — covering file manipulation, encoding, compression, and privilege escalation — then demonstrate social engineering attack vectors using the Browser Exploitation Framework (BeEF) to understand client-side threat models.

## Tools and Technologies

- **OverTheWire Bandit** — SSH-based wargame for Linux CLI training
- **BeEF (Browser Exploitation Framework)** — client-side attack framework
- **Linux CLI** — `cat`, `find`, `strings`, `grep`, `sort`, `uniq`, `base64`, `xxd`, `gzip`, `bzip2`, `tar`
- **Kali Linux** — operating environment

## Methodology

### Part 1: Linux Command-Line Challenges (Bandit Levels 0-12)

Solved 13 progressively difficult challenges requiring creative use of Linux utilities:

| Level | Challenge | Technique |
|-------|-----------|-----------|
| 0 | Read a file | `cat readme` |
| 1 | File named `-` | `cat ./-` (path disambiguation) |
| 2 | Filename with spaces | Backslash escaping |
| 3 | Hidden file | `ls -al` to reveal dotfiles |
| 4 | Identify human-readable file | `find . -type f \| xargs file` to check MIME types |
| 5 | File by size | `find . -type f -size 1033c ! -executable` |
| 6 | File by owner/group/size | `find / -type f -user bandit7 -group bandit6 -size 33c` |
| 7 | Search by keyword | `strings data.txt \| grep "millionth"` |
| 8 | Find unique line | `sort data.txt \| uniq -c` (count occurrences) |
| 9 | Extract from binary | `strings data.txt \| grep "="` |
| 10 | Base64 decoding | `base64 -d data.txt` |
| 11 | ROT13 cipher | Character substitution decoding |
| 12 | Nested compression | Iterative `xxd`, `gzip`, `bzip2`, `tar` decompression through 6+ layers |

### Part 2: Social Engineering with BeEF

Launched the BeEF framework on Kali and hooked a target browser through a demo page. Executed six attack modules from the BeEF control panel:

1. **Clippy Attack** — fake assistant prompt tricking users into downloading a malicious executable
2. **Fake Notification Bar** — spoofed browser notification mimicking a legitimate IE update prompt
3. **Drive-by Download** — served a file using alternative Content-Disposition headers to trigger automatic download
4. **Google Phishing** — rendered a fake Gmail login page with authentic favicon and styling to harvest credentials
5. **Pretty Theft** — injected a floating login dialog overlay to capture username/password input
6. **TabNabbing** — silently redirected an inactive tab to a phishing page, exploiting user inattention

## Key Findings

- **File system challenges demonstrate real sysadmin skills** — handling special characters, hidden files, binary data extraction, and multi-layer compression are everyday tasks in security operations
- **Level 12 (nested compression) mirrors real obfuscation techniques** — malware authors use layered compression to evade signature-based detection
- **BeEF requires zero server-side exploitation** — all attacks execute entirely through the hooked browser, demonstrating that fully patched servers are still vulnerable to client-side attack vectors
- **Social engineering bypasses technical controls** — phishing overlays, fake notifications, and tab manipulation exploit human trust rather than software vulnerabilities
- **Defense requires user awareness + technical controls** — Content Security Policy, XSS filters, and browser sandboxing mitigate these attacks, but user training remains the most effective countermeasure
