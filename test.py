import requests

def upload_file(filepath, url):
    filename = filepath.split('\\')[-1].split('/')[-1]
    with open(filepath, 'rb') as f:
        response = requests.post(
            url,
            files={'file': (filename, f, 'application/octet-stream')}
        )
    print("Server response:", response.text)

upload_file("recording_2026-03-14_22-05-27.wav", "https://www.cranneymccabe.com/test/truth/upload.php")