# 📦 All Modules
import speech_recognition as sr
import pyttsx3
import os
import subprocess
import time
import wikipedia
import requests
import json

# 🌤 Weather System Config
API_KEY = "1f0c62c501adcc58296bea23ee7590d8"  # Apni API key daalo
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# 🔊 Initialize speech engine
engine = pyttsx3.init()

# 📂 Profile file path
PROFILE_FILE = "profile.json"

# --- Profile load/save functions ---
def load_profile():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as f:
            return json.load(f)
    else:
        return None

def save_profile(profile):
    with open(PROFILE_FILE, "w") as f:
        json.dump(profile, f, indent=4)

# --- Setup profile if not exists ---
profile = load_profile()
if profile is None:
    print("Let's set up your profile first.")
    profile = {
        "name": input("Enter your name: "),
        "age": int(input("Enter your age: ")),
        "city": input("Enter your city: "),
        "hobby": input("Enter your hobby: "),
        "skills": input("Enter your skills (comma separated): ").split(","),
        "college": input("Enter your college name: ")
    }
    save_profile(profile)
    print("✅ Profile saved!")
else:
    print(f"Welcome back, {profile['name']}!")

# 👋 Greeting at startup
def greet_user():
    current_hour = time.localtime().tm_hour
    if 5 <= current_hour < 12:
        greeting = f"Good Morning {profile['name']}!"
    elif 12 <= current_hour < 17:
        greeting = f"Good Afternoon {profile['name']}!"
    elif 17 <= current_hour < 21:
        greeting = f"Good Evening {profile['name']}!"
    else:
        greeting = f"Hello {profile['name']}, hope you're having a peaceful night."

    engine.say(greeting)
    engine.say("How may I help you.")
    engine.runAndWait()

greet_user()

# 📚 Wikipedia search
def search_wikipedia(query):
    try:
        engine.say("Searching Wikipedia sir...")
        engine.runAndWait()

        result = wikipedia.summary(query, sentences=2)
        print("📖 Wikipedia Result:", result)
        engine.say("According to Wikipedia, " + result)
        engine.runAndWait()

    except wikipedia.exceptions.DisambiguationError:
        engine.say("Too many results found. Please be more specific.")
        engine.runAndWait()
    except wikipedia.exceptions.PageError:
        engine.say("Sorry, I couldn't find anything on Wikipedia.")
        engine.runAndWait()
    except Exception as e:
        engine.say("An error occurred while searching Wikipedia.")
        engine.runAndWait()
        print("❌ Error:", e)

# 🛠 Command execution
def command_execution(txt):
    txt = txt.lower()

    # --- Tell profile ---
    if "tell me about me" in txt or "my profile" in txt:
        details = f"Your name is {profile['name']}. You are {profile['age']} years old. You live in {profile['city']}. Your hobby is {profile['hobby']}. Your skills are {', '.join(profile['skills'])}. You study at {profile['college']}."
        print(details)
        engine.say(details)
        engine.runAndWait()

    # 1️⃣ WEATHER SYSTEM
    elif "weather" in txt or "temperature" in txt:
        engine.say("Checking the weather for you, sir.")
        engine.runAndWait()

        city = txt.replace("weather", "").replace("temperature", "")
        city = city.replace("in", "").replace("(", "").replace(")", "").replace(",", "").strip()

        if city == "":
            city = profile["city"]

        params = {"q": city, "appid": API_KEY, "units": "metric"}
        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()
            if data["cod"] == 200:
                temp = data["main"]["temp"]
                weather_desc = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]

                weather_report = f"The weather in {city} is {weather_desc} with a temperature of {temp}°C and humidity of {humidity}%."
                print(weather_report)
                engine.say(weather_report)
                engine.runAndWait()
            else:
                error_msg = data.get("message", "Unknown error")
                engine.say(f"Sorry, I couldn't find weather information for {city}. Reason: {error_msg}")
                engine.runAndWait()
        except Exception as e:
            print("Error fetching weather:", e)
            engine.say("Sorry, there was an error fetching the weather.")
            engine.runAndWait()

    # 2️⃣ HOW ARE YOU
    elif "how are you" in txt or "how's it going" in txt or "how are you doing" in txt:
        engine.say(f"I'm great {profile['name']}! How's your life going?")
        engine.runAndWait()

    # 3️⃣ YOUTUBE
    elif "youtube" in txt:
        engine.say("Turning on YouTube sir.")
        engine.runAndWait()
        os.startfile("https://www.youtube.com")

    # 4️⃣ CHROME
    elif "chrome" in txt:
        engine.say("Turning on Chrome sir.")
        engine.runAndWait()
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    # 5️⃣ VS CODE
    elif "vs code" in txt:
        engine.say("Turning on VS Code sir.")
        engine.runAndWait()
        subprocess.Popen("D:\\CODING SETUP\\Microsoft VS Code\\Code.exe")

    # 6️⃣ MUSIC
    elif "music" in txt:
        engine.say("Enjoy your best music.")
        engine.runAndWait()
        os.startfile("D:\\AI Project with Chat GPT\\simple project 3\\project stuffs\\Music\\Saiyaara-320kbps.mp3")

    # 7️⃣ MINECRAFT
    elif "minecraft" in txt:
        engine.say("Enjoy your best gaming experience.")
        engine.runAndWait()
        os.startfile("C:\\Users\\new\\OneDrive\\Desktop\\M Centers 5.0 beta Enable Trial.lnk")

    # 8️⃣ EDGE
    elif "edge" in txt:
        engine.say("Turning on Microsoft Edge sir.")
        engine.runAndWait()
        subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

    # 9️⃣ THANKS
    elif "thanks" in txt or "thankyou" in txt:
        engine.say("Most welcome sir. Have a great day.")
        engine.runAndWait()

    # 🔟 TIME
    elif "what is the time" in txt or "time" in txt:
        current_hour = time.localtime().tm_hour
        if 5 <= current_hour < 12:
            greeting = "Good Morning"
        elif 12 <= current_hour < 17:
            greeting = "Good Afternoon"
        elif 17 <= current_hour < 21:
            greeting = "Good Evening"
        else:
            greeting = "It's late night. Take some rest!"

        current_time = time.strftime("%I:%M %p")
        full_response = f"{greeting} {profile['name']}. The time is {current_time}."
        print(full_response)
        engine.say(full_response)
        engine.runAndWait()

    # 1️⃣1️⃣ WIKIPEDIA
    elif "who is" in txt or "what is" in txt or "tell me about" in txt or "wikipedia" in txt:
        search_query = txt.replace("who is", "").replace("what is", "").replace("tell me about", "").replace("wikipedia", "")
        search_wikipedia(search_query.strip())

    else:
        print("❓ Command not recognized 🤷‍♂️")
        engine.say("Sorry, I did not understand the command.")
        engine.runAndWait()

# 🎤 Speech recognition loop
r = sr.Recognizer()
mic_index = 2  # Apne mic index ke hisaab se change karo

while True:
    with sr.Microphone(device_index=mic_index) as source:
        print("\n🎙️ Adjusting to background noise...")
        r.adjust_for_ambient_noise(source, duration=2)

        print("🎧 Speak now... (5 seconds max)")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("🧠 Recognizing...")
        
            text = r.recognize_google(audio)
            print("🗣️ You said:", text)
            command_execution(text)

        except sr.WaitTimeoutError:
            print("⏰ Timeout: Mic didn't catch anything")
        except sr.UnknownValueError:
            print("🤷 Could not understand your speech.")
        except sr.RequestError:
            print("📡 Network/API issue!")






