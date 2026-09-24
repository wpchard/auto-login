import subprocess
import time

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

subprocess.Popen([
    chrome,
    "--profile-directory=Profile 2",   # Replace with your school profile
    "https://mail.google.com/"
])

time.sleep(5)  # Wait for Chrome to open