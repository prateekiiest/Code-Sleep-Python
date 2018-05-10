# Speech-To-Text

Simple Script to get User input from microphone and use Google's API to transform into text.

# Installation

Install python-pyaudio:

```
sudo apt-get install python-pyaudio
```

Install portaudio:

```
sudo apt-get install portaudio19-dev
```

Sadly, the PyAudio is not updated and doesn't work on the latest version of Python3 so:

```
virtualenv -p python2.7 req
source req/bin/activate
pip install PyAudio
pip install SpeechRecognition
```

# Test the app:

```
source req/bin/activate
python stt.py
```

# TODO:

- Find a way to make this work for Python3.

- Add new recognition APIs.