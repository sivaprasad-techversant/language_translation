from google.cloud import texttospeech
import os

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="Hello, World!")

# Build the voice request
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary
with open(r"C:\Users\SIVA\Techversant Training\voice_assistant\data\output\G_output\output.wav", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

# Play the synthesized audio file
os.system("start output.mp3")
