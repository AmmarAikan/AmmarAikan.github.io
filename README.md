# Ammar Aikan — Cybersecurity CV

A static CV-focused website, distinct from the main Firebase portfolio. Its professional facts and seven project/lab entries are generated from the shared verified career source. Training, coursework, team contributions and fork hardening retain their attribution. The `#profile` anchor remains stable.

## Public content policy

This repository contains only sanitized professional material. Internal IP addresses, hostnames, accounts, packet captures, exploit payloads, scanner output, and confidential client or training infrastructure details are intentionally excluded.

## Files

- `index.html` - accessible, printable single-page CV
- `assets/styles.css` - responsive layout and print styles
- `assets/app.js` - progressive navigation highlighting; content and links work without it
- `assets/cv/` - validated two-page PDF and editable DOCX
- `assets/Ammar-Aikan-CV.pdf` - compatibility URL serving the same current validated PDF
- `assets/images/` - original-photograph optimizations and derived favicons
- `assets/socialguard-f1.png` - project evidence visual from the SocialGuard report
- `assets/reports/` - permanently sanitized public portfolio reports, including the co-authored Veeam backup and recovery lab

The generated site is static and needs no runtime build or third-party JavaScript. Hosting remains GitHub Pages `main:/`; no migration is introduced. Existing public reports remain preserved.

The content generator is `Career Branding Workspace/sites/cv-build.py` beside the private factual source and CV generator. It verifies the CV source hash before copying downloads and rendering this website. Private evidence and internal reports are not copied into the public repository. Update central content, regenerate/validate the CV, run the site generator, then review and deploy through existing Pages hosting.

The Google Drive link is explicitly a CV folder. Publishing a fresh local PDF here does not upload it to that folder.
