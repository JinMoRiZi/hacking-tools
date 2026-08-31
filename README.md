# Hacking Tools

A collection of penetration testing tools built from scratch in Python.

## Port Scanner (portscanner.py)

A multithreaded port scanner with service detection and banner grabbing.

### Features
- Scans ports 1-1024 simultaneously using threading
- Identifies service names for each open port
- Grabs version banners from live services

### Usage
python3 portscanner.py

### Example Output
Port 21 | ftp | 220 (vsFTPd 2.3.4)
Port 22 | ssh | SSH-2.0-OpenSSH_4.7p1
