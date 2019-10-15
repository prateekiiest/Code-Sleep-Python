import speech_recognition as sr

r = sr.Recognizer()
flag = 1
while flag=1:
    
    with sr.Microphone() as source:
        print("Say something... ")
        audio = r.listen(source)

    try:
        print("Google thinks you said: {}".format(r.recognize_google(audio)))
        flag = 0
    except sr.UnkownValueError:
        print("Couldn't understand your voice. Please speak again.")
    except sr.RequestError as e:
        print("Couldn't request results. Please speak again.; {}".format(e))
