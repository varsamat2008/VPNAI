import tkinter as tk
from tkinter import messagebox
import webbrowser
import random
import datetime
import pyttsx3  # For text-to-speech functionality
import requests  # For fetching weather, news, etc.

# Initialize text-to-speech engine
engine = pyttsx3.init()

class JarvisAssistant:
    def __init__(self, master):
        self.master = master
        self.master.title("Jarvis AI Assistant")
        self.master.geometry("400x600")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Welcome to Jarvis AI!", font=("Arial", 18))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Execute", command=self.execute_command)
        self.submit_button.pack(pady=10)

        self.output_text = tk.Text(self.master, height=15, width=50)
        self.output_text.pack(pady=10)

    def execute_command(self):
        command = self.entry.get().lower()
        self.output_text.delete(1.0, tk.END)

        if "open" in command:
            self.open_website(command)
        elif "joke" in command:
            self.tell_joke()
        elif "time" in command:
            self.tell_time()
        elif "weather" in command:
            self.get_weather()
        elif "news" in command:
            self.get_news()
        elif "translate" in command:
            self.translate(command)
        else:
            self.output_text.insert(tk.END, "Command not recognized.")

    def open_website(self, command):
        url = command.split("open")[-1].strip()
        webbrowser.open(url)
        self.output_text.insert(tk.END, f"Opening {url}")

    def tell_joke(self):
        jokes = ["Why did the scarecrow win an award? Because he was outstanding in his field!",
                 "I told my computer I needed a break, and now it won't stop sending me KitKat ads."]
        self.output_text.insert(tk.END, random.choice(jokes))

    def tell_time(self):
        now = datetime.datetime.now()
        self.output_text.insert(tk.END, f"The current time is {now.strftime('%H:%M:%S')}")

    def get_weather(self):
        # Sample weather API call (needs a real API key)
        api_key = "6e242acf5e4d62c3937d13954225f892"
        city = "London"  # Example city
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        if data["cod"] != "404":
            main = data["main"]
            temp = main["temp"] - 273.15  # Convert from Kelvin to Celsius
            self.output_text.insert(tk.END, f"Current temperature in {city} is {temp:.2f}°C")
        else:
            self.output_text.insert(tk.END, "City not found.")

    def get_news(self):
        # Sample news API call (needs a real API key)
        api_key = "YOUR_API_KEY"
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)
        articles = response.json()["articles"]
        headlines = "\n".join([article["title"] for article in articles[:5]])
        self.output_text.insert(tk.END, f"Top headlines:\n{headlines}")

    def translate(self, command):
        # Placeholder for translation logic
        self.output_text.insert(tk.END, "Translation feature not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    jarvis = JarvisAssistant(root)
    root.mainloop()
