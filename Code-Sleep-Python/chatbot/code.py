import speech_recognition as sr
import os
import subprocess
from gtts import gTTS

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
    print("Got the speech. Now processing...")

# recognize speech using Wit.ai
# export your wit.ai key to your environment before running this program
WIT_AI_KEY = os.getenv("WITAIKEY")
if not WIT_AI_KEY:
    print("API key not available")
    exit()

in_speech = ""
try:
    in_speech = r.recognize_wit(audio, key=WIT_AI_KEY)
    print("You said " + in_speech)
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

# in_speech contains the string of the input audio.
# It can be processed and actions can be performed based on it.
# TODO implement actions based on keywords
# Suggestions: Utilise wit.ai for proper NLP

if (in_speech):
    tts = gTTS(text=in_speech, lang="en")
    tts.save("sample.mp3")
    subprocess.Popen(["mpg123", "-q", "sample.mp3"]).wait()
