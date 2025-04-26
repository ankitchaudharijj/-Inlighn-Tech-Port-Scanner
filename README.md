
# Port Scanner Tool

A Python-based tool to scan a target host for open ports within a specified range, identifying services and grabbing banners where possible.

---

## 📋 Project Description

This tool scans a given target IP address or domain for open TCP ports.  
It identifies running services, captures banners when available, and displays results in a color-coded table.

The tool uses **multithreading** to perform fast scanning, and dynamically updates progress in the terminal.

---

## 🚀 Features

- Fast multithreaded port scanning
- Banner grabbing from open ports
- Service name detection
- Color-coded terminal output (green for open ports)
- Progress tracking during scanning

---

## 🛠️ Prerequisites

- **Python 3.x** installed (no external libraries needed)

---

## 📂 Project Structure

```
Port_Scanner_Project/
|
├── port_scanner.py      # Main port scanner script
└── README.md             # Project documentation
```

---

## 📜 Usage Instructions

1. **Clone the repository** or download the files.

2. **Run the script**:
   ```bash
   python port_scanner.py
   ```

3. **Provide input when prompted**:
   - Enter target hostname or IP address.
   - Enter the starting and ending ports.

4. **View results**:
   - Open ports, service names, and banners are printed in a formatted table.

---

## 📈 How It Works

- Resolves the hostname to an IP address.
- Scans ports using TCP connections (`socket` module).
- Identifies the service associated with each open port.
- Grabs the banner (if available) from open ports.
- Displays results using ANSI color codes.
- Tracks and displays progress dynamically.

---

## ✨ Example Output

```
[*] Starting scan on 45.33.32.156 from port 20 to 100...

PORT       SERVICE         BANNER                        
------------------------------------------------------------
22         ssh             OpenSSH 7.4                   
80         http            Apache/2.4.29 (Ubuntu)         

Enumeration complete.
```

---

## 👨‍💻 Author

**Ankit Chaudhari**  
Cybersecurity Enthusiast | Ethical Hacker | Network Auditor

- **University:** Delhi Skill and Entrepreneurship University
- **Certification:** Certified Ethical Hacker (CEH v12)
- **Skills:** Cybersecurity, Ethical Hacking, Network Auditing, VAPT
- **GitHub:** [@ankitchaudharijj](https://github.com/ankitchaudharijj)
- **LinkedIn:** [Ankit Chaudhari](https://www.linkedin.com/in/ankit-chaudhari-40346b318/)

---

## 📄 License

This project is intended for **educational purposes** and **ethical use only**.  
Unauthorized malicious use is strictly prohibited.

---

# 🛡️ Happy Hacking! 🚀
