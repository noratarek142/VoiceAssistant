# VoiceAssistant
Voice Assistant with Reminder Functionality

Overview:

This project is a voice-controlled assistant built in Python, capable of recognizing speech commands and providing responses. The assistant can tell the current time and date, set reminders, and play music. It integrates various libraries such as SpeechRecognition, gTTS, and plyer to provide a seamless user experience.
Features:
    Voice Recognition: Uses Google’s Speech Recognition API to understand user commands.
    Text-to-Speech: Converts responses into speech using Google Text-to-Speech (gTTS).
    Reminder Functionality: Allows users to set reminders for specific times with desktop notifications.
    Current Time and Date: Provides real-time updates of the current time and date.
    Music Playback: Can play music from YouTube based on voice commands.

Requirements

Make sure you have the following libraries installed:

-playsound
-gtts
-speech_recognition
-datetime
-re
-threading
-subprocess
-pywhatkit

You can install the required libraries using pip:
example: pip install playsound gtts SpeechRecognition pywhatkit

Installation:
1-Clone the repository 

example: git clone <repository-url>
         cd <repository-directory>
2-Install the required libraries:

example: pip install -r requirements.txt

3- Ensure microphone access: Make sure your microphone is set up and working correctly on your system.

Usage:
1-Run the assistant:
  python Alexa.py

2-Available Commands:

    Hi: The assistant will greet you.
    Time: The assistant will tell you the current time.
    Date: The assistant will provide the current date.
    Reminder at HH
    : Set a reminder for the specified time (e.g., “Set a reminder at 14:30”).
    Bye: Exit the assistant.

3-Set a Reminder:

    To set a reminder, say a command like: “Set a reminder at 14:30”.
    You will receive a notification at the specified time.
Example:
User: Hi
Assistant: Hello!

User: What time is it?
Assistant: The time is 14:30.

User: Set a reminder at 15:00.
Assistant: Reminder set for 15:00.


Acknowledgements:

gTTS - Google Text-to-Speech
SpeechRecognition - Library for speech recognition
plyer - Cross-platform API for notifications


