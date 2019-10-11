from gtts import gTTS

text = input("Enter the text you want to convert: ")
tts = gTTS(text=text, lang='en')
tts.save("speech.mp3")
