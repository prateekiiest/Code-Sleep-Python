import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something... ")
    audio = r.listen(source)

try:
    print("Google thinks you said: {}".format(r.recognize_google(audio)))
except sr.UnkownValueError:
    print("Couldn't understand")
except sr.RequestError as e:
    print("Couldn't request results; {}".format(e))
