import pyttsx3
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

name = input("Enter your name:" )

age = input("Enter your age: ")

print("Welcome to the AI VARSAM" + name)
speak("Welcome to the AI VARSAM..." + name)

if '17' in age:
    print("Ok sir welcome to the this tool......")
    speak("Ok sir welcome to the this tool......")
    function = input("Enter which function can i do optional : 1. Webs opening :")
    if 'webs opening' in function:
        speak("Tell me which website can i open it that....")
        web = input("Enter which website can i open that : ")
        if 'youtube' in web:
            webbrowser.open('https://www.youtube.com')
            speak("Opening youtube...")
        elif 'google' in web:
            webbrowser.open('https://www.google.com')
            speak("Opening google...")
        elif 'open my website' in web:
            webbrowser.open('https://www.varsamai.blogspot.com')
            speak("Opening varsamai website...")
        elif 'open cloud shell' in web:
            webbrowser.open('https://www.shell.cloud.google.com')


    

else:
    speak("Enter the correct age and try to fill 17 age....")

