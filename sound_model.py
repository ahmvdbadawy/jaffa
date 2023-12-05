import speech_recognition as sr
import pyttsx3
import random
import tkinter as tk

start_sig_input = ["hello", "hi", "hey", "good morning", "hey palestine", "hi palestine", "hi yafa", "hi "]
start_sig_output = ["hey", "My name is yafa, how can i help you", "yes sir", "any thing", "any time", "hi there", "good morning", ""]
recognizer = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def recognize_speech(audio):
    try:    
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Sorry, there was an error processing your request."
    
def db_search(key):
    file = open("db.csv", 'r')
    for x in file.readlines():
        x = x.split()
        print(x)
    

def display(text):
    engine = pyttsx3.init()
    if str(text).lower() in start_sig_input:
        random.choice(start_sig_input)
        engine.say(random.choice(start_sig_output))
        engine.runAndWait()
    print(text)

if __name__ == "__main__":
    # audio = record_audio()
    # display(recognize_speech(audio))
    db_search('anas')
