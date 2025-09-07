from jarvis.tts import speak
from jarvis.stt import listen
import webbrowser

def main():
    speak("Hello, I am Jarvis. Say my name to activate me. Say 'stop' anytime to quit.")

    while True:
        command = listen().lower()
        print(f"User said: {command}")
        if "stop" in command:
            speak("Goodbye! Shutting down.")
            break

        if "jarvis" in command:
            speak("Yes, I am listening. What’s your command?")
            task = listen().lower()
            print(f"Command: {task}")
            if "stop" in task:
                speak("Goodbye! Shutting down.")
                break
            else:
                speak(f"You said: {task}")


if __name__ == "__main__":
    main()
