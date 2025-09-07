from jarvis.tts import speak

def main():
    message = "Hello, I am Jarvis. How can I help you?"
    print(message)   # Prints in terminal
    speak(message)   # Speaks out loud

if __name__ == "__main__":
    main()
