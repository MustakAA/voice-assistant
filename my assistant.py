import pyttsx3
from gtts import gTTS

a=input('say something :')
tts = gTTS(text=a, lang='bn')
print (tts)
engine=pyttsx3.init()
def bolo(text):
    engine.say(text)

if 'কেমন আছ' in a:
    text='I am fine'
    bolo(text)
if 'কি খবর' in a:
    text='Not bad'
    bolo(text)
engine.runAndWait()
