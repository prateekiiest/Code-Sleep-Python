from gtts import gTTS

text=("Hello world!")
tts = gTTS(text=text, lang='en')
tts.save("speech.mp3")
