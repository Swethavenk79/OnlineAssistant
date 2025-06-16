# Voice-Based Assistant using Python

A simple voice assistant that listens to your voice and performs basic tasks like telling the time, checking the weather in any city, opening websites, and searching Google — all using your voice!

---

## Features

- Tells the current time
- Speaks weather for **any city worldwide** using OpenWeatherMap
- Searches Google
- Opens YouTube
- Opens Google Chrome (if installed in the default location)

---

## Requirements

Install these Python libraries:

```bash
pip install speechrecognition pyttsx3 requests
```

Also install `pyaudio` (for microphone access on Windows):

```bash
pip install pipwin
pipwin install pyaudio
```

---

## Weather Setup

1. Go to [https://openweathermap.org](https://openweathermap.org)
2. Sign up and get a **free API key**
3. In the script, replace this line:

```python
api_key = "your_api_key_here"
```

with your actual API key.

---

## How to Run

Use the command line or Git Bash:

```bash
python voice_assistant.py
```

Then speak commands like:

- "What's the time?"
- "Open YouTube"
- "Weather in Paris"
- "Search artificial intelligence"

## Note

Ensure your microphone is working and your internet is connected for voice recognition and weather features.
