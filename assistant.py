import pyttsx3
import speech_recognition as amit
import datetime
import wikipedia
import webbrowser
import os

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")

    speak("I am your assistant sir. Please tell me how may I help you")

def takecommand():
    # it takes microphone input from the user and retern string output

    r = amit.Recognizer()
    with amit.Microphone() as source:
        print("Listening...")
        r.pause_threshold =3
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, Language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query = takecommand().lower()
    # logic for executing task based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.com")

        elif 'open codechef' in query:
            webbrowser.open("codechef.com")

        elif 'play video' in query:
            video_dir = 'D:\\video hd'
            videos = os.listdir(video_dir)
            print(videos)
            os.startfile(os.path.join(video_dir,videos[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is{strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Aman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


