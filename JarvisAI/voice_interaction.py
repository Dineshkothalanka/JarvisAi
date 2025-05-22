"""
Module for handling voice interactions: speech-to-text and text-to-speech.
"""

import speech_recognition as sr
import pyttsx3

class VoiceInteraction:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""

    def speak(self, text):
        self.engine.say(text)
        try:
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in text-to-speech: {e}")
