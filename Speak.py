from package import *

engine = pyttsx3.init()
def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
  
