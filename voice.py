import pyttsx3

engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

speak("hello veeresh i a varsam the virtual artificial robot system of all machine......")