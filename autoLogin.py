import subprocess
import time

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

subprocess.Popen([
    chrome,
    "--profile-directory=Profile 2",
    "https://mail.google.com/"
])

time.sleep(5)  # wait for chrome to open