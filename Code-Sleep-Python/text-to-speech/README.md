# Text-To-Speech

This code uses the gtts library to read a textinput and create an mp3 file. Very simple but very cool.

Create a virtualenv using python3 and install the requirements with:

```
virtualenv -p python3 req
source req/bin/activate
pip install -r requirements.txt
```

To run the app just do: 
```
python tts.py
```

For the first version the text is just hard coded inside the file but next step is to make the app take an optional input like:

```
python tts.py -t "Some random text that we want in an mp3 file"
```
