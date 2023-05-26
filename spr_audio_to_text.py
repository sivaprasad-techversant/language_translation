import speech_recognition as spr
recog = spr.Recognizer()

noisyspeech = spr.AudioFile("C:/Users/SIVA/Techversant Training/speech_recognition/input/audio2.wav")
with noisyspeech as noisesource:
    recog.adjust_for_ambient_noise(noisesource)
    audio = recog.record(noisesource)

print(recog.recognize_google(audio))