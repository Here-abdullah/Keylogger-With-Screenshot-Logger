# 🔐 Advanced Keylogger (For Ethical Use Only)

This is an **ethical keylogger** built in Python for **Blue Team / SOC Analyst** training and **endpoint activity monitoring**. It logs keystrokes and periodically captures screenshots, storing them securely with optional encryption.

> ⚠️ For **educational and ethical use only**. Do not deploy without consent.

---

## 📂 Features

- Logs **keystrokes** and saves them in timestamped files.
- Periodically captures **screenshots** (default: every 10 seconds).
- Stores logs in separate folders for better organization.
- Uses **AES encryption** for log protection.
- Auto-generates and uses a secure `secret.key` file.
- Option to email or upload logs can be added later.

---

## 🧰 Libraries Used

| Library        | Purpose                                      |
|----------------|----------------------------------------------|
| `pynput`       | Captures keyboard input                      |
| `pyautogui`    | Takes screenshots                            |
| `cryptography` | Encrypts keylogs using Fernet (AES)         |
| `threading`    | Handles keylogging and screenshot in parallel |
| `datetime`     | For timestamps                               |
| `os`, `time`   | File handling and delays                     |

Install all dependencies using:

```bash
pip install pynput pyautogui cryptography
```

---

## 🛠 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Keylogger-Advanced.git
cd Keylogger-Advanced
```

### 2. Run the Keylogger

```bash
python keylogger_advanced.py
```

### 3. Stop the Keylogger

Press `Ctrl + C` or close the terminal window.

---

## 📁 Output Structure

- `keylogger_logs/keys/` — Saved keystroke logs.
- `keylogger_logs/screen/` — Captured screenshots.
- `secret.key` — Encryption key file.

---

## ✅ Notes

- Logs are encrypted with Fernet (AES) encryption.
- Compatible with Python 3.8+.
- Screenshots are stored in high-quality PNG format.

---

## 🔒 Legal Disclaimer

This tool is for **educational purposes only**. Do not use without permission on any system. Unauthorized use is illegal.