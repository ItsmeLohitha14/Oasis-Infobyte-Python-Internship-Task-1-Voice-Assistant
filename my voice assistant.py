import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import random


engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<16:
        speak("Good Afternoon")

    else:
        speak("Good Evening")  

    speak("Hello friendss Iam your voice assistant How may I assist you")      


def takecommand():
    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language ='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        print("Say that again please...")    
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'interesting facts' in query:
            facts = [
            "The shortest war in history lasted only 38 minutes.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion.",
            "Bananas are berries, but strawberries aren't.",
            "The Great Wall of China is not visible from space without aid.",
            "Octopuses have three hearts and blue blood.",
            ]
            speak("Here's an interesting fact for you:")
            speak(random.choice(facts))  

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"Mam, time is{strTime}")   


        elif 'date' in query:
            strdate = datetime.datetime.now().strftime("%d:%m:%Y")    
            speak(f"Mam, date is{strdate}")  

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif "play" in query:
            song = query.replace('play', "Copines(Lyrics)")
            speak("Playing" + song)
            pywhatkit.playonyt(song)    
        

        elif 'open code' in query:
            codepath="D:\sdc2 snake"
            os.startfile(codepath)
         

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Sorry, I can only understand basic commands for now.")
    

  
