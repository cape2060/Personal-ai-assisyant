import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import pywhatkit
import datetime
import os
import time
import requests


listener =sr.Recognizer()

def bolne(text):
    # Initialize the text-to-speech engine;
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  #changing voice from male to female 0=male 1=female;
    engine.say(text)
    engine.runAndWait()
    

def sunne():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice=listener.listen(source)
            text=listener.recognize_google(voice,language='en-ne')
            
            print("You:",text)

    except:
        print(f"Could not request results")
    return text
def close(app):
    try:
        os.system(f"taskkill /f /im {app}")
        print(f"Closing {app}...")
        bolne(f"Closing {app}...")
    except Exception as e:
        print(f"Error: {e}")
        bolne("Sorry, could not close the application.")
def main():
    while 1:
        command =sunne()
        command=command.lower()
        if "hello alexa" in command:
            assistant()
        sites=[["facebook","https://facebook.com"],
               ["instagram","https://instagram.com"],
               ["youtube","https://youtube.com"],
               ["google","https://google.com"],
               ["twitter","https://twitter.com"],
               ["linkedin","https://linkedin.com"],
               ["high anime","https://hianimez.to"],
               ["rare toon india","https://www.rareanimes.com"]]
        for site in sites:
            if f"open {site[0]}" in command:
                bolne(f"Opening {site[0]}...")
                firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
                webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
                webbrowser.get('firefox').open(site[1])
                break
        if "play" in command:
            song=command.replace("play","")
            pywhatkit.playonyt(song)
            bolne(f"Playing {song}...")
        elif "time" in command:
            time1=datetime.datetime.now().strftime("%I:%M %p")
            print(f"The time is {time1}")
            bolne(f"The time is {time1}")
        elif "date" in command:
            date=datetime.datetime.now().date()
            print(f"Today's date is {date}") 
            bolne(f"Today's date is {date}")       
        elif "search" in command:
            khojne=command.replace("search", "")
            try:
                result = wikipedia.summary(khojne, 5)
                print(result)
                bolne(result)
                
            except wikipedia.exceptions.DisambiguationError as e:
                print("Multiple results found, try to be more specific.")
                bolne("Multiple results found, try to be more specific.")
                print(e.options)  # Print the options
        elif "open zoom" in command:
            bolne("Opening zoom...")
            path=r"your application loication where zoom exe file is located"
            os.startfile(path)
            time.sleep(5)
        elif "close zoom" in command:
            close("Zoom.exe")
        elif "close browser" in command:
            close("msedge.exe")
        elif "exit" in command:
            bolne("Exiting...")
            exit()
    
def assistant():
    print("🤖 Assistant (Alexa) ready. Type 'exit' to quit.")
    bolne("🤖 Assistant Alexa ready. Type 'exit' to quit.")
    while True:
        input = sunne()
        if input.lower() in {"exit"}:
            print("Assistant: Goodbye!")
            break
        response = alexa(input)
        print("Assistant:", response)
        bolne(response)

def alexa(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2",  # or other model you have pulled
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"[Error connecting to Ollama]: {e}"
    

         

if __name__=="__main__":
        main()
