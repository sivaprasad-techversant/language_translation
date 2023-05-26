import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="<your-subscription-key>", region="<your-service-region>")
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

text = "Hello, world!"
result = synthesizer.speak_text_async(text).get()

with open(r"C:\Users\SIVA\Techversant Training\voice_assistant\data\output\MA_output\output.wav", "wb") as out:
    out.write(result.audio_data)
