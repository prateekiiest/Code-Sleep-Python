import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def sendemail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("mygmai.com","my password")
    server.sendmail("mygmail.com",to,content)
    server.close()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("Good evening sir")

    speak("I am Friday, your virtual assistant running on python?")
    speak("How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)

        print("Please repeat your command..")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        speak("According to what i found on wikipedia")
        print(results)
        speak(results)
    elif 'what can you do' in query:
        speak("I can search for something in wikipedia,")
        speak("open websites, play friends or even open your whatsapp.")
        speak("If you are interested to  read some amazing blogs say open my blog.")
    elif 'who are you' in query:
        speak("I am friday, the successor of Jarvis.")
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open instagram' in query:
        webbrowser.open("instagram.com")
    elif 'open my blog' in query:
        webbrowser.open("codehustler.dev")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'open whatsapp' in query:
        subprocess.call(
            'C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
    elif 'email to name' in quary:
        try:
            speak("email_content")
            content = takecommand()
            to = "abc@gmail.com"
            sendemail(to, content)
            speak("email has been sent")
        except Exception as e:
            print(e)
            speak("sorry my friend unable to send email")
    elif 'play friends' in query:
        friends_dir = 'G:\\F.R.I.E.N.D.S'
        friends = os.listdir(friends_dir)
        print(friends)
        os.startfile(os.path.join(friends_dir, friends[0]))
    elif 'terminate' in query:
        speak("Goodbye sir see you soon.")
        exit()
