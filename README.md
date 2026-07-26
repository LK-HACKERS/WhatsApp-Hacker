```markdown
# 📱 LK-HACKERS WhatsApp Hacking Tool

> **⚠️ IMPORTANT DISCLAIMER: This tool is for EDUCATIONAL and AUTHORIZED SECURITY TESTING purposes only. Use only on systems you own or have explicit permission to test. The authors are not responsible for any misuse.**

---

## 📌 Overview

**LK-HACKERS WhatsApp Hacking Tool** is an advanced security testing tool designed for WhatsApp security research. It demonstrates various attack vectors including account hijacking, group takeover, and channel compromise.

**🔴 WARNING: This is a DEMONSTRATION tool for security awareness. Do NOT use for illegal activities.**

---

## 🎯 Features

| Feature | Description | Status |
|---------|-------------|--------|
| 📱 **Number Hack** | Hijack WhatsApp accounts via OTP relay | ✅ Active |
| 👥 **Group Hijack** | Takeover WhatsApp groups | ✅ Active |
| 📢 **Channel Hack** | Compromise WhatsApp channels | ✅ Active |
| 🚫 **Banned** | Check account/group/channel ban status | ✅ Active |
| 📂 **Logging** | Auto-save all captured data | ✅ Active |
| 🎨 **Dark UI** | Professional hacker-themed interface | ✅ Active |

---

## 📂 Files Generated

| File | Description |
|------|-------------|
| `logs/whatsapp_number_YYYYMMDD.txt` | Captured target numbers |
| `logs/whatsapp_otp_YYYYMMDD.txt` | Captured OTP codes |
| `logs/whatsapp_group_YYYYMMDD.txt` | Captured group links |
| `logs/whatsapp_channel_YYYYMMDD.txt` | Captured channel links |
| `logs/whatsapp_hijack_success_YYYYMMDD.txt` | Successful hijack logs |

---

## 🚀 Installation

### 📱 Termux (Android)
```bash
pkg update && pkg upgrade
pkg install python
pip install flask
git clone https://github.com/LK-HACKERS/WhatsApp-Hacker.git
cd whatsapp-hacker
python run.py
```

🐧 Kali Linux / Ubuntu

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install flask
git clone https://github.com/LK-HACKERS/whatsapp-hacker.git
cd whatsapp-hacker
python3 run.py
```

💻 Windows

```bash
# Install Python from python.org
pip install flask
git clone https://github.com/LK-HACKERS/whatsapp-hacker.git
cd whatsapp-hacker
python run.py
```

🍎 macOS

```bash
brew install python3
pip3 install flask
git clone https://github.com/LK-HACKERS/whatsapp-hacker.git
cd whatsapp-hacker
python3 run.py
```

---

💻 Usage Guide

1️⃣ Start the Server

```bash
python run.py
```

2️⃣ Access the Tool

Open your browser and navigate to:

```
http://localhost:5000
```

3️⃣ Main Menu

```
┌─────────────────────────────────────────────┐
│         LK-HACKERS WhatsApp Hacking         │
│                                             │
│  ┌──────────┐  ┌──────────┐                │
│  │ 📱       │  │ 👥       │                │
│  │ Number    │  │ Group    │                │
│  │ Hack      │  │ Hijack   │                │
│  └──────────┘  └──────────┘                │
│                                             │
│  ┌──────────┐  ┌──────────┐                │
│  │ 📢       │  │ 🚫       │                │
│  │ Channel   │  │ Banned   │                │
│  │ Hack      │  │          │                │
│  └──────────┘  └──────────┘                │
└─────────────────────────────────────────────┘
```

---

📱 Number Hack (Account Hijacking)

Step 1: Enter Target Details

```
📱 WhatsApp Account Hijack

Target Phone Number (with country code)
[ +94712345678 ]

Your WhatsApp Number (for OTP relay)
[ +94718765432 ]

[ 🚀 SEND OTP REQUEST ]
```

Step 2: OTP Verification

```
🔐 OTP Verification

Enter the OTP received on your WhatsApp number
[ • • • • • • ]

[ ✅ VERIFY & HIJACK ]

OTP was sent to: +94712345678
```

Step 3: Success!

```
🏆 HIJACK SUCCESSFUL!

Target: +94712345678
Status: ✅ ACCOUNT COMPROMISED
Access: FULL CONTROL
```

---

👥 Group Hijack

Step 1: Enter Group Details

```
👥 WhatsApp Group Hijack

Target Group Invite Link
[ https://chat.whatsapp.com/xxxxx ]

Your WhatsApp Number
[ +94718765432 ]

[ 🚀 HIJACK GROUP ]
```

Step 2: Success!

```
👥 GROUP HIJACKED!

Group: https://chat.whatsapp.com/xxxxx
Status: ✅ GROUP COMPROMISED
Access: FULL ADMIN CONTROL
```

---

📢 Channel Hack

Step 1: Enter Channel Details

```
📢 WhatsApp Channel Hack

Target Channel Link
[ https://whatsapp.com/channel/xxxxx ]

Your WhatsApp Number
[ +94718765432 ]

[ 🚀 HACK CHANNEL ]
```

Step 2: Success!

```
📢 CHANNEL HACKED!

Channel: https://whatsapp.com/channel/xxxxx
Status: ✅ CHANNEL COMPROMISED
Access: FULL ADMIN CONTROL
```

---

🚫 Banned Page

```
🚫 ACCOUNT BANNED

⚠️ The target account/group/channel has been BANNED by WhatsApp.

This could be due to suspicious activity or violation of 
WhatsApp's Terms of Service.

[ ⬅ BACK TO MENU ]
```

---

📂 Log Files Structure

```bash
logs/
├── whatsapp_number_20250115.txt
├── whatsapp_otp_20250115.txt
├── whatsapp_group_20250115.txt
├── whatsapp_channel_20250115.txt
└── whatsapp_hijack_success_20250115.txt
```

Example Log:

```
[2025-01-15 14:23:45] Target: +94712345678 | Attacker: +94718765432
[2025-01-15 14:25:12] OTP: 123456 | Target: +94712345678
[2025-01-15 14:25:30] ACCOUNT HIJACKED: +94712345678
```

---

🛡️ Security Features

Feature Description
🔒 Local Hosting No external servers involved
🔐 No Tracking All data stays locally
📂 Local Logging Plain text logs (no encryption)
🌐 Local Network Runs on localhost only

---

💀 Pro Tips

Tip Description
🔒 Use VPN Hide your real IP address
📱 Use Burner Numbers Don't use your real number
🧹 Clear Logs Delete logs after use
🌐 Use Tor For extra anonymity
🧽 Clear History Clear browser history after use

---

⚠️ Legal & Ethical Use

This tool is intended for:

· ✅ Security awareness training
· ✅ Penetration testing (with permission)
· ✅ Educational demonstrations
· ✅ Red team exercises
· ✅ Vulnerability research

DO NOT use this tool for:

· ❌ Stealing WhatsApp accounts
· ❌ Unauthorized access
· ❌ Any illegal activities
· ❌ Fraud or identity theft
· ❌ Harassment or stalking

---

🔧 Troubleshooting

Problem Solution
Port already in use pkill -f python
Flask not installed pip install flask
Permission denied chmod +x run.py
Can't access browser Use http://127.0.0.1:5000
No logs saving Create logs/ folder
Invalid phone number Use correct format: +94712345678

---

📊 System Requirements

Requirement Minimum
Python 3.6+
Flask Latest
RAM 256MB
Storage 50MB
Network Localhost

---
📱 OS Compatibility

OS Status
Windows ✅ Works
Linux (Ubuntu/Kali) ✅ Works
macOS ✅ Works
Termux (Android) ✅ Works
iOS (iSH) ✅ Works

---

🚀 Future Updates

· Auto-OTP capture
· Multiple number support
· Proxy support
· Tor integration
· Auto-clean logs
· Export reports
· GUI desktop app

---

📝 License

MIT License - See LICENSE file for details.

---

👨‍💻 Author

LK-HACKERS
CYBER BLACK LION

· Telegram: @LKHACKERS
· YouTube: SL Cyber Scanners
· GitHub: LK-HACKERS

---

⭐ Support

If you find this useful, please ⭐ Star the repository and share it responsibly.

---

🛡️ Security Advisory

⚠️ REMEMBER: With great power comes great responsibility!

· Use this tool only for educational purposes
· Get explicit permission before testing
· Follow all applicable laws
· Respect others' privacy
· Report vulnerabilities responsibly

---

© 2026 LK-HACKERS. All rights reserved.


