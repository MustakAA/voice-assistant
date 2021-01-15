import pyttsx3
from gtts import gTTS

a=input('say something :')
tts = gTTS(text=a, lang='bn')
print (tts)
engine=pyttsx3.init()
def bolo(text):
    engine.say(text)

if 'kemon aso' in a:
    text='I am fine'
    bolo(text)
if 'ki khobor' in a:
    text='Too good'
    bolo(text)
engine.runAndWait()
