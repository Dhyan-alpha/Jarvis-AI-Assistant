import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='en-in')
        return command.lower()
    except:
        return "none"

speak("Hello Dhyan, I am Jarvis")

while True:
    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")

    elif "wikipedia" in command:
        speak("Searching Wikipedia")
        command = command.replace("wikipedia", "")
        result = wikipedia.summary(command, sentences=2)
        speak(result)

    elif "open google" in command:
        webbrowser.open("https://google.com")

    elif "exit" in command or "quit" in command:
        speak("Goodbye")
        break
