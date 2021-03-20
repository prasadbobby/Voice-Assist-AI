from Package import *                                                                         # importing packages from Package.py file
from Speak import *                                                                           # importing speak() function from Speak.py
from CPU import *                                                                             # importing cpu() function from CPU.py
from DateTime import *                                                                        # importing date() and time() from DateTime.py
from Jokes import *                                                                           # importing jokes() from Jokes.py
from ScreenShot import *                                                                      # importing screenshot() from Screenshot.py
from SendMail import *                                                                        # importing sendMail() from SendMail.py
from TakeCommand import *                                                                     # importing takeCommand() from TakeCommand.py
from Hour import *                                                                            # importing hour() from Hour.py 


# If you need complete code in a single file then go to "Assistant.py" in this directory.
# If you want to run the code in your machine, then install all the packages from Package.py file and cross-check whether all the packages are installed correctly.

if __name__ == "__main__":                                                                    # main function of the project.                                               
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
            songs_dir = 'D:\\Music'                                                            # in songs_dir variable you can add your own path of music.
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
            
        # create a new file named "data.txt" and place the file in the same directory.
        elif 'remember that' in query:
            speak("What should I remember? ")
            data = takeCommand()
            speak("you said me to remember "+data)
            remember = open('data.txt', 'w')
            remember.wriet(data)
            remember.close()                                                                    

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
