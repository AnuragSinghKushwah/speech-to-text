from gtts import gTTS
import os

# Calling Speech to Text Engine
tts = gTTS(text='Good morning', lang='en')

# Saving To MP3
tts.save("good.mp3")

#Using mpg321 to speak out the output file
os.system("mpg321 good.mp3")