# src/jarvis/app.py
from jarvis.tts import speak
from jarvis.stt import listen
import webbrowser, os, re, urllib.parse

# Predefined site shortcuts
SITE_MAP = {
    "google": "https://www.google.com",
    "facebook": "https://www.facebook.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
}

def normalize(text: str) -> str:
    if not text:
        return ""
    s = text.lower()
    s = s.replace(" dot com", ".com").replace(" dot ", ".").replace(" dotcom", ".com")
    s = re.sub(r"[^a-z0-9\.\s\-]", "", s)
    return s.strip()

def open_url(url: str):
    if not url.startswith("http"):
        url = "https://" + url
    try:
        webbrowser.open_new_tab(url)
        print(f"Opened: {url}")
        return True
    except:
        return False

def handle_task(task: str):
    task = normalize(task)

    if task.startswith("open "):
        target = task.split("open ", 1)[1].strip()
        if not target:
            speak("Open what?")
            return
        if target in SITE_MAP:
            open_url(SITE_MAP[target])
            speak(f"Opening {target}")
        elif "." in target:  # looks like a domain
            if open_url(target):
                speak(f"Opening {target}")
            else:
                speak(f"Sorry, I couldn't open {target}")
        else:  # fallback search
            query = urllib.parse.quote_plus(target)
            open_url(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {target}")
        return

    if "search" in task.lower():
        query = task.split("search ", 1)[1].strip()
        if query:
            open_url(f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}")
            speak(f"Searching for {query}")
        else:
            speak("Search what?")
        return

    speak(f"You said: {task}")

def main():
    speak("Hello, I am Jarvis. Say my name to activate me. Say 'stop' anytime to quit.")

    while True:
        command = normalize(listen())
        if not command:
            continue

        print("User said:", command)

        if "stop" in command:
            speak("Goodbye! Shutting down.")
            break

        if "jarvis" in command:
            speak("Yes, what's your command?")
            task = normalize(listen())

            if "stop" in task:
                speak("Goodbye! Shutting down.")
                break

            if task:
                handle_task(task)
