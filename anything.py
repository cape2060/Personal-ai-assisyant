import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import pywhatkit
import datetime
import os
import time
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from portscanner import scanner, checking
from remove import remover
from subdomain import nikalne,find
from hashcraker import hash_type, md5_hashchecker, sha1_hashchecker, sha256_hashchecker, sha512_hashchecker, sha224_hashchecker, sha384_hashchecker
from passgen import generator
from gmail import data
from brutforce import details, brutforce
from dirfinder import wordset, bypass403 , ok_200, forbidden_403
from autorevengi import check, check1


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
        elif "hash" in command:
            print("Welcome to the Hash Cracker!")
            bolne("Welcome to the Hash Cracker!")
            print("ENter the hash you want to crack:")
            bolne("Enter the hash you want to crack:")
            hash=input()
            
            bolne("Checking hash type...")
            integer=hash_type(hash)
        
            print("Do you want to crack the hash (yes/no)")
            bolne("Do you want to crack the hash yes or no")
            answer=input()
            answer=answer.lower()
            if answer == "yes":
                print("Please provide the path to your custom wordlist:")
                bolne("Please provide the path to your custom wordlist:")
                list = input()
            
            else:
                sunne()
            
            if integer==1:
                md5_hashchecker(list,hash)
            elif integer==2:
                sha1_hashchecker(list,hash)
            elif integer==3:
                sha256_hashchecker(list,hash)
            elif integer==4:
                sha512_hashchecker(list,hash)
            elif integer==5:
                sha224_hashchecker(list,hash)
            elif integer==6:
                sha384_hashchecker(list,hash)
            else:
                print("I do not know how to crack this hash type")
                bolne("I do not know how to crack this hash type") 
        elif "password" in command:
            print("Generating a random password...")
            bolne("Generating a random password...")
            generator()
        elif "send email" in command:
            print("Welcome to the Email Sender!")
            bolne("Welcome to the Email Sender!")
            print("This tool sends an email with attachments.")
            bolne("This tool sends an email with attachments.")
            print("Do you want to send an email? (yes/no): ")
            bolne("Do you want to send an email? (yes/no): ")
            ball = input().strip().lower()

            if "y" in ball:
                data()
            else:
                print("Exiting the Email Sender. Goodbye!")
                bolne("Exiting the Email Sender. Goodbye!")
        elif "brute force" in command:
            url,username,name,name1,text,loc=details()
            print("Brutforcing the password...")
            bolne("Brutforcing the password...")
            brutforce(url, username, name, name1,text, loc)
        elif "find directory" in command:
            print("Enter the target url:")
            bolne("Enter the target url:")
            url=input().strip()
            print("Enter the wordlist file path:")
            bolne("Enter the wordlist file path:")
            dir=input().strip()
            print("Starting directory search...")
            bolne("Starting directory search...")
            wordset(url, dir)
            print(Fore.CYAN + f"200 ok directories: {ok_200}" + Style.RESET_ALL)    
            print(Fore.RED + f"403 Forbidden directories: {forbidden_403}" + Style.RESET_ALL) 
            print("Directory search completed.")
            bolne("Directory search completed.")
            print("You want to bypass the 403 directories? (yes/no)")
            bolne("You want to bypass the 403 directories? (yes/no)")
            choice = input().strip().lower()
            if 'y' in choice:
                print("Give me the url by adding th 403 dir find in search in list(e.g. https://example.com/403dir):")
                bolne("Give me the url by adding the 403 dir found in search in list")
                url1 = input().strip()
                print("Bypassing the 403 directory...")
                bolne("Bypassing the 403 directory...")
                bypass403(url1)
        elif "reverse engineer" in command:
            print("\033[1;32mEnter the path of file for reverse engineering and find the password:")
            bolne("Enter the path of file for reverse engineering and find the password:")
            path=input().strip()
            print("\033[92mDo you want to put the address of the line where correct password is printed or use that string instead(string/address)")
            bolne("Do you want to put the address of the line where correct password is printed or use that string instead(string/address)")
            choice = input().strip().lower()
            if 'string' in choice:
                print("\033[92mEnter the string which is printed when correct password is entered:")
                bolne("Enter the string which is printed when correct password is entered:")
                string = input().strip()
                def correct(input):
                    return string.encode() in input.posix.dumps(1)
                print("\033[92mStarting reverse engineering...")
                bolne("Starting reverse engineering...")  
                
                check(path,correct)

            else:
                print("\033[92mEnter the address of the line where correct password is printed(0x123123123):")
                bolne("Enter the address of the line where correct password is printed:")
                address = input().strip()
                print("\033[92mStarting reverse engineering...")
                bolne("Starting reverse engineering...")    
                check1(path,address)
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
