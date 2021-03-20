from Package import *
from Speak import *

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+usage)
    battery = psutil.sensors_battery()
    speak("The battery percent is")
    speak(battery.percent)
