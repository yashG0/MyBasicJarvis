import datetime
from winreg import QueryReflectionKey
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os


# Setting the robo-voice from microsoft API -  
engine = pyttsx3.init('sapi5')

# Set Property of voice 
voices = engine.getProperty('voices')

# Display Property of voice [0] - male , [1] - female
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour<=12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("This is Jarvis , Sir please tell me how can i help you...")

def takeCommand():
    # Its takes microsphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}")
    except Exception as e:
        print(e)
        print("Say that again please..")
        return "None"
    return query

if __name__ == '__main__':
    # speak("this is john")
    wishMe()

    while True:
        query = takeCommand().lower()

    # Logic for executing task based on query
        if wikipedia in query:
            speak('Searching in Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            # webbrowser.open("https://www.spotify.com/in-en/")
            MyMusicDirectory = 'C:\\Users\\yashg\\Music'
            songs = os.listdir(MyMusicDirectory)
            print(songs)
            os.startfile(os.path.join(MyMusicDirectory,songs[0]))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H %M %S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\Users\yashg\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
            os.startfile(codepath)
        
        else:
            print("Not any command, idiot")
            speak("Not any command, idiot")

            


    