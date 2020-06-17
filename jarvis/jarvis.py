import wikipedia
import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
# import twitter
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
global chrome
from bot import path
from bot import Url_name
from bot import login




global hour
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12) :
        print(hour)
        speak("Good Morning!")
    elif (hour>=12 and hour<=18):
        print(hour)
        speak("Good Afternoon")
    else:
        print(hour)
        speak("Good evening")

    speak("I am Jarvis sir,please tell me how can i help you!")
def takeCommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    # takeCommand() 
    # while True:
    while 1:
        query="open instagram"
        # query="shahrukh khan wikipedia"
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("Wikipedia"," ")
            results =wikipedia.summary(query,sentences=2)
            speak("Accordoing to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir="D:\\personal\\asutosh comm\\Desktop\\songs\\songs\\songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            codePath=r"C:\\Users\Naman Crist\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open instagram' in query:
            path()
            Url_name()
            login("username","password")
            exit()

 

        
