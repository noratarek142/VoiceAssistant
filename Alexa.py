import os
import playsound
from gtts import gTTS
import speech_recognition as sr
import datetime
import re
from threading import Timer
import subprocess
import webbrowser  
import pywhatkit

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
lang = "en"

def speak(text):
    tts = gTTS(text=text, lang=lang)
    tts.save("response.mp3")
    playsound.playsound("response.mp3")
    os.remove("response.mp3")

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.datetime.now().strftime("%A %m/%d/%Y")

def listen():
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise. Please wait...")
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            voice = r.listen(source, timeout=5)
            print("Processing...")
            command = r.recognize_google(voice, language=lang)
            print(f"You said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak("Sorry, there was a problem with the speech recognition service.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred. Please repeat.")
        return ""

def extract_time(command):
    # Look for any pattern matching HH:MM
    time_match = re.search(r'\b([01]?\d|2[0-3]):([0-5]\d)\b', command)
    if time_match:
        return time_match.group(0)
    return None

def set_reminder(time_str):
    def reminder():
        print("Reminder function called")  # Debugging print statement
        speak("Reminder!")
        print("Reminder!")

    try:
         # Use notify-send to show a notification
        subprocess.run(['notify-send', 'Test Notification', 'reminder is set, Nora'])
        # Regular expression to match HH:MM format
        time_match = re.match(r'^([01]?\d|2[0-3]):([0-5]\d)$', time_str)
        if not time_match:
            speak("Please use the HH:MM format.")
            print("Invalid time format. Please use HH:MM.")
            return

        reminder_time = datetime.datetime.strptime(time_str, "%H:%M").time()
        now = datetime.datetime.now().time()
        
        reminder_seconds = ((reminder_time.hour - now.hour) * 3600 +
                            (reminder_time.minute - now.minute) * 60)

        if reminder_seconds < 0:
            reminder_seconds += 86400  # Add a full day if the time is in the past

        # Print reminder seconds for debugging
        print(f"Reminder will be triggered in {reminder_seconds} seconds")

        # Check if Timer starts
        Timer(reminder_seconds, reminder).start()
        print("Timer started")
        speak(f"Reminder set for {time_str}.")
        print(f"Reminder set for {time_str}.")
    except ValueError:
        speak("There was an error processing the time.")
        print("Invalid time format. Please use HH:MM.")

def extract_time(command):
    # Look for any pattern matching HH:MM
    time_match = re.search(r'\b([01]?\d|2[0-3]):([0-5]\d)\b', command)
    if time_match:
        return time_match.group(0)
    return None       

def run():
    while True:
        command = listen()
        if command:
            if 'bye' in command:
                speak("Goodbye!")
                break
            elif 'hi' in command:
                speak("Hello!")
            elif 'time' in command:
                speak("The time is " + get_time())
            elif 'date' in command:
                speak("The date is " + get_date())
            elif 'reminder' in command:
                time_str = extract_time(command)  # Extract time from the command
                if time_str:
                    set_reminder(time_str)
                else:
                    speak("Please specify the time for the reminder in HH:MM format.")
            elif 'song' in command or 'music' in command:
                pywhatkit.playonyt(command.replace('Alexa', ''))
            elif 'linkedin' in command:
                speak("Opening your LinkedIn.")
                webbrowser.open("https://www.linkedin.com/in/nora-tarek-011048223/")  # Open LinkedIn   
            elif 'google' in command:
                speak("Opening google browser.")
                webbrowser.open("https://www.google.com/")  # Open google        

# Start the assistant
run()
