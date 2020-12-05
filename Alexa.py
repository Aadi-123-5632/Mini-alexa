import pyttsx3
import datetime
import speech_recognition as sr
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
if __name__ == "__main__":
    wishMe()     