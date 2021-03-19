from Package import *
from Speak import *
def time():
  time = datetime.datetime.now().strftime("%I:%M:%S")
  speak(time)
  
def date():
  date = int(datetime.datetime.now().day)
  month = int(datetime.datetime.now().month)
  year = int(datetime.datetime.now().year)
  speak(date)
  speak(month)
  speak(year)
  
  
  
