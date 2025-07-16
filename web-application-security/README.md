# Web Application Security

Exploitation and analysis of common web vulnerabilities — Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF) — using Google's Gruyere intentionally vulnerable web application, with defensive countermeasure analysis.

## Objective

Demonstrate four web attack vectors (File Upload XSS, Reflected XSS, Stored XSS, CSRF) against a controlled vulnerable application, analyze the root cause of each vulnerability, and identify effective countermeasures for production web applications.

## Tools and Technologies

- **Google Gruyere** — intentionally vulnerable web application for security testing
- **Custom HTML/JavaScript payloads** — crafted attack scripts
- **Web browser** — attack execution environment
- **Kali Linux** — operating environment

## Methodology

### Attack 1: File Upload XSS

**Technique:** Uploaded an HTML file containing embedded JavaScript to the application's file upload feature.

```html
<script>alert("XSS")</script>
```

**Process:** Logged into Gruyere, navigated to Upload, uploaded the HTML file, accessed the uploaded file's URL directly.

**Result:** The JavaScript executed in the browser — confirming arbitrary script execution via uploaded content.

**Root Cause:** The server served uploaded files with their original MIME type (`text/html`) instead of forcing `text/plain`. No content-type validation on upload.

**Countermeasures:** Serve uploads as `text/plain` or `application/octet-stream`, host uploads on a sandboxed subdomain, block HTML/SVG uploads, implement CSP headers.

### Attack 2: Reflected XSS

**Technique:** Injected a script payload directly into the URL, which the server reflected back into the page HTML without sanitization.

```
https://target-app/<instance>/<script>alert("Reflected XSS")</script>
```

**Result:** The browser rendered the injected script and executed the alert.

**Root Cause:** User input from the URL path was echoed directly into the response without HTML encoding.

**Countermeasures:** Escape all user input before reflecting in HTML output, use templating engines with automatic output escaping (Jinja2 autoescape, React JSX), deploy CSP to block inline scripts.

### Attack 3: Stored XSS

**Technique:** Created a snippet containing an HTML anchor tag with a malicious `onmouseover` event handler.

```html
<a href="#" onmouseover="alert('Stored XSS')">Hover me</a>
```

**Result:** The stored payload persisted in the database and executed for every user who viewed the snippet — a persistent attack affecting all visitors.

**Root Cause:** Snippet content was stored and rendered without sanitization. Event handler attributes were not stripped.

**Countermeasures:** Use a whitelist-based HTML sanitizer (DOMPurify, Bleach), normalize and validate HTML tags against an allow-list, apply CSP `script-src` directives.

### Attack 4: Cross-Site Request Forgery (CSRF)

**Technique:** Created an external HTML page containing a hidden image tag whose `src` pointed to the snippet deletion endpoint.

```html
<img src="https://target-app/<instance>/deletesnippet?index=0" style="display:none">
```

**Process:** While logged into the app in one tab, opened the CSRF page in another tab. The browser automatically sent the authenticated GET request.

**Result:** Snippet at index 0 was silently deleted without any user interaction or confirmation.

**Root Cause:** Destructive actions were performed via GET requests with no anti-CSRF token validation. The server relied solely on session cookies.

**Countermeasures:** Require POST/PUT/DELETE for state-changing operations, include anti-CSRF tokens in forms, set `SameSite=Strict` on session cookies, verify `Origin` and `Referer` headers.

## Key Findings

- **XSS variants target different injection points** — File Upload exploits content-type handling, Reflected exploits URL parameter echoing, Stored exploits persistent data rendering
- **Stored XSS is the most dangerous variant** — the payload persists and executes for every visitor, enabling credential theft, session hijacking, and malware distribution at scale
- **CSRF exploits implicit trust in cookies** — browsers automatically attach cookies to every request, allowing forged cross-origin requests to execute authenticated actions
- **GET for mutations is a critical design flaw** — using GET for destructive operations violates HTTP semantics and enables trivial CSRF via image tags and link prefetching
- **Defense requires layered controls** — input validation, output encoding, CSP headers, SameSite cookies, and anti-CSRF tokens must work together
