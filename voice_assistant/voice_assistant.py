import speech_recognition as sr  # type: ignore
import pyttsx3  # type: ignore
import datetime
import webbrowser
import random
engine = pyttsx3.init()
engine.setProperty('rate', 150)  
engine.setProperty('volume', 1.0) 
ASSISTANT_NAME = "Nova"
greetings = [
    "Hi there! I'm Nova, your virtual assistant.",
    "Hello! Nova at your service.",
    "Greetings! Nova here to help you out.",
]
def speak(text):
    print("Nova:", text)
    engine.say(text)
    engine.runAndWait()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Oops! I didn’t get that. Could you try again?")
            return ""
        except sr.RequestError:
            speak("Hmm, I can't connect to the internet right now.")
            return ""
def respond(command):
    if "hello" in command or "hi" in command:
        speak(random.choice([
            "Hello again!",
            "Hi there! What can I do for you?",
            "Hey! Ready to assist you.",
        ]))
    elif "your name" in command:
        speak(f"My name is {ASSISTANT_NAME}, your personal assistant.")
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")
    elif "date" in command:
        date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {date}")
    elif "search" in command:
        speak("What would you like me to search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Searching Google for {query}")
    elif "exit" in command or "stop" in command:
        speak("Alright, shutting down. Take care!")
        exit()
    else:
        speak("Hmm, I'm still learning. I don't understand that yet.")
speak(random.choice(greetings))
current_time = datetime.datetime.now().strftime("%I:%M %p")
current_date = datetime.datetime.now().strftime("%A, %B %d")
speak(f"It's {current_time} on {current_date}.")
speak("You can ask me things like 'what time is it', 'what's today's date', or 'search something online'.")
while True:
    user_command = listen()
    if user_command:
        respond(user_command)