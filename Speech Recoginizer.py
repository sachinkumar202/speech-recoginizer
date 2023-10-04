#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr


# In[ ]:


import pyttsx3

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
text_to_speech = pyttsx3.init()

# Function to listen to user's voice command
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError as e:
            print(f"Sorry, there was an error with the request: {e}")
            return ""

# Function to execute user's command
def execute_command(command):
    if "hello" in command:
        text_to_speech.say("Hello! How can I assist you?")
        text_to_speech.runAndWait()
    elif "what is your name" in command:
        text_to_speech.say("I am a Python-based virtual assistant. You can call me Jarvis.")
        text_to_speech.runAndWait()
    elif "exit" in command:
        text_to_speech.say("Goodbye!")
        text_to_speech.runAndWait()
        exit()
    else:
        text_to_speech.say("I'm not sure how to do that.")
        text_to_speech.runAndWait()

# Main loop
while True:
    command = listen_for_command()
    execute_command(command)


# In[ ]:





# In[ ]:




