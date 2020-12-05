import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >> 0 and hour<12:
        speak(" Hey Good morning")
    elif hour >=12 and hour < 18:
        speak(" Hey Good afternoon")
    else:
        speak(" Hey good evening")
    speak("Sir or ma'am I m Alexa your personal assistant. Please tell how may i help you") 
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold=1
        audio =r.listen(source)
    try:
        print("Rocognising.....")
        query=r.recognize_google(audio, language="en-in")  
        print(f"User said: {query}\n")   
    except Exception as e :
        print("Sir say that again please")
        return"None"
    return query
if __name__ == "__main__":
    wishMe()
    while True: 
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query= query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=4)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open rec sonbhadra' in query:
            webbrowser.open("http://recsonbhadra.ac.in/")
        elif 'play romantic music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=QBR45OLRbw4")
        elif 'play sad music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=LRzR6MenPvU")
        elif 'play music' in query:
            music_dir="C:\\Users\\aadi\\Desktop\\videos"
            songs=os.listdir(music_dir)
            print(songs)
            d=random.choice(songs)
            os.startfile(os.path.join(music_dir,d))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H: %M: %S")
            print(strtime)
            speak(f"Sir the time is{strtime}")
        elif 'open coding platform' in query:
            codePath="C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)