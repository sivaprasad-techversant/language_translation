import requests

url = "https://api.murf.ai/tts"
headers = {"x-api-key": "<your-api-key>"}
params = {"text": "Hello, world!", "voice": "en-US-Wavenet-D", "format": "mp3"}

response = requests.get(url, headers=headers, params=params)

with open(r"C:\Users\SIVA\Techversant Training\voice_assistant\data\output\Murf_output\output.wav", "wb") as out:
    out.write(response.content)
