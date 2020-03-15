import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)

r = int(random.randrange(0,7))
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Jarvis sir ,How may i help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising..")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}")

    except Exception as e:
        print("Say that again please...")
        return None
    return query

def sendemail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('singhsimran1802@gmail.com','finn@8802060479')
    server.sendmail('singhsimran1802@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishme()
    # while True:
    if 1:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.co.in")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'E:\\New folder\\ Root\\Users\\Kamal\\Desktop\\icons\\new'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[r]))

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is :{time}")
            print(time)

        elif 'who are you' in query:
            speak('I am jarvis sir')
            

        elif 'open netbeans' in query:
            code_path = "C:\\Program Files\\NetBeans 8.0.1\\bin\\netbeans64.exe"
            os.startfile(code_path)

        # elif 'open ms word' or 'microsoft word' or 'word' in query:
        #     word_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office"
        #     word = os.listdir(word_path)
        #     print(word)
        #     os.startfile(os.path.join(word_path,word[9]))

        elif 'open taken3' or 'open game' in query:
            game_path = "C:\\Users\\Gagan\\Desktop\\New folder"
            game = os.listdir(game_path)
            print(game)
            os.startfile(os.path.join(game_path,game[0]))

        elif 'mail to me' in query:
            try:
                speak('What should i say?')
                content = takecommand()
                to = "singhsimran1802@gmail.com"
                sendemail(to,content)
                speak("Email has been sent successfully")

            except Exception as e:
                print(e)
                speak("I am not able to send your email, Please try again!!")










