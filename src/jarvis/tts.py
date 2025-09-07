import pyttsx3
def list_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    for i, voice in enumerate(voices):
        print(f"[{i}] {voice.name} ({voice.id})")
def speak(text: str):
    engine = pyttsx3.init()
    rate=engine.getProperty("rate")
    voices=engine.getProperty("voices")
    volume=engine.getProperty("volume")
    engine.setProperty("rate", 220) 
    engine.setProperty("voice", voices[1].id) 
    list_voices()
    print(rate,volume)
    engine.say(text)
    engine.runAndWait()
