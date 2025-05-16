import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import pywhatkit
import datetime
import os
import time
import requests
from portscanner import scanner, checking
from remove import remover
from subdomain import nikalne,find


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

    except Exception as e:
        print("Could not hear you properly,please speak again clearly")
        bolne("Could not hear you properly,please speak again clearly")
        return sunne()
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
            path=r"C:\Users\HP\AppData\Roaming\Zoom\bin\Zoom.exe"
            os.startfile(path)
            time.sleep(5)
        elif "scan" in command:
            print("Enter the target ip address or domain name:")
            bolne("Enter the target ip address or domain name")
            target=sunne()
            length=checking(target)
            while True:   
                if length==True:
                    print("Valid IP address")
                    bolne("Valid IP address")
                    break
                else:
                    print("Invalid IP address")
                    bolne("Invalid IP address")
                    bolne("Please enter a valid IP address by typing it")
                    target=input()
                    length=checking(target)
                

            print("Enter the port you want yo scan from 1 to 65535")
            bolne("Enter the port you want yo scan from 1 to 65535(starting port)")
            starting=sunne()
            print("Enter the port you want yo scan from 1 to 65535")
            bolne("Enter the port you want yo scan from 1 to 65535(ending port)")
            ending=sunne()
            bolne("Scanning...")
            scanner(target, starting, ending)
            print("Scanning completed.")
            bolne("Scanning completed.")
        elif "remove background" in command:
            print("Enter the location of image:")
            bolne("Enter the location of image:")
            inputpath=input().strip()#use the hello folder as input as well as outputth path
            if not os.path.isfile(inputpath):
                print("File not found")
                bolne("File not found")
                exit(1)
            print("Enter the location where you want to save the image:")   
            bolne("Enter the location where you want to save the image:")
            outputpath=input().strip()#use location eg:c:/hello/ball.png
          
            bolne("Removing background...")
            print("Removing background...")
            
           
            remover(inputpath,outputpath)
            print("Background removed successfully.")
            bolne("Background removed successfully.")
        elif "subdomain"in command:
            bolne("Enter the name of domain")
            domain=sunne().strip()
            bolne("Enter the wordlist path")
            filepath=input("ENter the wordlidt path:").strip()
            
            if not os.path.isfile(filepath):
                print("File not found")
                bolne("File not found")
                exit(1)
            print("Extracting domain form list")
            bolne("Extracting domain form list")
            wordlist=nikalne(filepath)
            a=find(domain, wordlist)
            

            if a:
                print("Subdomian found")
                for subdomain in a:
                    print(f"{subdomain}")
            else:
                print("No subdomain found")

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
            bolne("Goodbye!,have a nice day.")
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
