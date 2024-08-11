from gtts import gTTS
from playsound import playsound

text_val = 'All the best for your exam.'
# Here are converting in English Language
language ='en'
gTTsobj = gTTS(text=text_val, lang=language, slow=False)
gTTsobj.save("exam.mp3")
playsound("exam.mp3")
