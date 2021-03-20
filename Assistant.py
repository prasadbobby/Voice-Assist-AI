# This is the main python of the project. This file contains all the code in a single file. You can run this file incase there is any error in the main.py file.


import pyttsx3                                                                                    # pip install pyttsx3
import datetime
import speech_recognition as sr                                                                   # pip install SpeechRecognition
import wikipedia                                                                                  # pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui                                                                                  # pip install pyautogui
import psutil                                                                                     # pip install psutil
import pyjokes                                                                                    # pip install pyjokes
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Hello world")


def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)


def hour():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening sir")


def sendMail(to, content):                                      # SendMail.py
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mahendragandham730@gmail.com', '12345678')
    server.sendmail('mahendragandham730@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-us')
        print(query)

    except Exception as e:
        speak("Unable to Recognize your voice. Make sure that you have a good internet connection.")
        return "None"

    return query


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+usage)
    battery = psutil.sensors_battery()
    speak("The battery percent is")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching..")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            query(result)

        elif 'send mail' in query:
            try:
                speak("What should I say? ")
                content = takeCommand()
                to = 'mahendrasaikumargandham@gmail.com'
                # sendEmail(to, content)
                speak(content)
                speak("E mail has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send Email, Please Check your internet connection")

        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = 'C:/Programming Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search)

        elif 'logout' in query:
            os.system("Shutdown -l")

        elif 'shutdown' in query:
            os.system("Shutdown /s /t 1")

            elif 'restart' in query:
            os.system("Shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should I remember? ")
            data = takeCommand()
            speak("you said me to remember "+data)
            remember = open('data.txt', 'w')
            remember.wriet(data)
            remember.close()
            # create a new file data.txt

        elif 'do you know' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that"+remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Screenhot taken")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            quit()
