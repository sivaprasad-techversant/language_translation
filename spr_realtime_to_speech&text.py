import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=0.2)

    audio2 = r.listen(source2)

    MyText = r.recognize_google(audio2)
    MyText = MyText.lower()
    Vision: Diversity & Inclusion is a
    critical
    part
    of
    our
    culture, driving
    business
    success and ensuring
    that
    all
    our
    employees
    feel
    they
    belong
    at
    RR
    Donnelley.Our
    customers, suppliers, and communities
    benefit
    from the wealth

    of
    ideas, innovations and focused
    solutions
    our
    diversity
    creates.
    print("Did you say - "+MyText)
    SpeakText(MyText)
