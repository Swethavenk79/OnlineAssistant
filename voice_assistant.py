import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import os
import requests

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("❌ Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("⚠️ Internet error.")
        return ""

def get_weather(city):
    api_key = "a6cf0bdfad333833fcb4fb76068819dc"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "404":
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            result = f"The weather in {city.title()} is {weather} with a temperature of {temp} degree Celsius."
            return result
        else:
            return "City not found."
    except:
        return "Unable to fetch weather at the moment."

def run_assistant():
    speak("Hello! How can I help you?")
    command = listen()

    if 'time' in command:
        current_time = datetime.now().strftime('%I:%M %p')
        speak(f"The time is {current_time}")

    elif 'open youtube' in command:
        webbrowser.open('https://www.youtube.com')
        speak("Opening YouTube")

    elif 'open chrome' in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            os.startfile(chrome_path)
            speak("Opening Google Chrome")
        else:
            speak("Chrome is not installed in the default location.")

    elif "weather" in command:
        speak("Which city?")
        city = listen().lower()
        weather_info = get_weather(city)
        speak(weather_info)

    elif 'search' in command:
        query = command.replace('search', '')
        url = f"https://www.google.com/search?q={query.strip()}"
        webbrowser.open(url)
        speak(f"Searching for {query.strip()}")

    else:
        speak("I didn't understand that.")

# Run the assistant
run_assistant()
