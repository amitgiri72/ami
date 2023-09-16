from http import server
from operator import truediv
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognize...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

# to wish
def wish():
    hour = (datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("Good Morning")

    elif hour>12 and hour<=18:
        speak("Good Afternoon")

    else :
        speak("Good Evening")

    speak("i am ati sir. please tell me how can i help you")

#send Email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rxvirat05@gmail.com','6392231675')
    server.sendmail('rxvirat05@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wish()

    while True:
    # if 1:

        query = takecommand().lower()
        # logic building for task
        if 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            speak("opening notepad sir...")
            os.startfile(npath)

        elif 'open code' in query:
            code = "C:\\Users\\Aman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening code sir...")
            os.startfile(code)

        elif 'open command prompt' in query:
            os.system("start cmd")
            speak("opening command prompt sir...")

        elif 'open camera' in query:
            speak("opening camera sir...")
            cap = cv2.VideoCapture(0)
            while True:
            
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            
            cv2.destroyAllWindows()

        elif 'play music' in query:
            speak("playing music sir..." )
            music_dir = "D:\\video hd"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif 'wikipedia' in query:
            speak("searching wikipedia... ")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            speak("sir what should i search on youtube")
            sh = takecommand().lower()
            pywhatkit.playonyt(f"{sh}")

        elif 'google' in query:
            speak("opening google sir...")
            speak("sir what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'codechef' in query:
            speak("opening gfg sir...")
            webbrowser.open("www.codechef.com")

        elif 'gfg' in query:
            speak("opening gfg sir...")
            webbrowser.open("www.geeksforgeek")

        elif 'send message' in query:
            pywhatkit.sendwhatmsg("+7070099770","this is testing",14,55)

        elif 'play song on youtube' in query:
           
            speak("sir which song i play on youtube")
            tm = takecommand().lower()
            pywhatkit.playonyt(f"{tm}")

        elif 'email to amit' in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                # to = takecommand().lower()
                to = "ag4982324@gmail.com"
                sendEmail(to,content)
                speak("Email has been send") 

            except Exception as e:
                print(e)
                speak("sorry sir, i failed to send the email") 

        elif 'thanks' in query:
            speak("thanks for using me sir ,have a Good Day.")
            sys.exit()

        speak("sir do you have any other task")


                 







    # takecommand()
    # speak("this is vishal apka naukar sir")