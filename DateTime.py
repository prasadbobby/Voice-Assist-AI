from Package import *                                               # import packages from Package.py file in the same directory
from Speak import *                                                 # import speak function from Speak.py file
def time():                                                         # Created time() function.
  time = datetime.datetime.now().strftime("%I:%M:%S")
  speak(time)                                                       # speak out the current time
  
def date():                                                         # created date() function.
  date = int(datetime.datetime.now().day)
  month = int(datetime.datetime.now().month)
  year = int(datetime.datetime.now().year)
  speak(date)                                                       # speak out the current date
  speak(month)                                                      # speak out the current month 
  speak(year)                                                       # speak out the current year
  
  
  
