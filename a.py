import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return None

    return query
def run_personal_assistant():
    while True:
        query = listen()

        if query:
            # Convert query to lowercase for easier processing
            query = query.lower()

            # Check for specific commands or keywords
            if 'wikipedia' in query:
                # Extract the search term from the query
                search_term = query.replace('wikipedia', '')
                search_results = wikipedia.summary(search_term, sentences=2)
                print(search_results)
                speak(search_results)
            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com")
            elif 'open google' in query:
                webbrowser.open("https://www.google.com")
            elif 'time' in query:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                print("Current time is: ", current_time)
                speak("The current time is " + current_time)
            elif 'quit' in query:
                break
            else:
                speak("Sorry, I didn't understand that command.")

run_personal_assistant()
