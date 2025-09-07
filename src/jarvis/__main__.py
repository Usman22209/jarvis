from jarvis.stt import listen
from jarvis.tts import speak

def main():
    speak("Hello, I am Jarvis. What should I do?")
    command = listen()
    print(f"User said: {command}")
    speak(f"You said: {command}")

if __name__ == "__main__":
    main()
