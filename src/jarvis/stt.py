import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    # If multiple mics exist, pass device_index (e.g., 1, 2, etc.)
    with sr.Microphone(device_index=None) as source:  
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I could not understand."
    except sr.RequestError:
        return "Sorry, speech service is unavailable."
