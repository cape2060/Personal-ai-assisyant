import string
import random
import pyttsx3
import speech_recognition as sr
def bolne(text):
    
  
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # changing voice
    engine.say(text)
    engine.runAndWait()
def sunne():
   
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            text = listener.recognize_google(voice, language='en-ne')
            print("You:", text)
    except Exception as e:
        print("Could not hear you properly, please speak again clearly.")
        bolne("Could not hear you properly, please speak again clearly.")
        return sunne()
    return text
def generator():
    firstpart=string.ascii_uppercase
    secondpart=string.ascii_lowercase
    thirdpart=string.digits
    fourthpart=string.punctuation

    total=firstpart+secondpart+thirdpart+fourthpart
    password = ''.join(random.sample(total, 18))
    print(f"Your password is: {password}")
    bolne(f"Your password is: {password}")
    print("You want to store this password in a file? (yes/no)")
    bolne("You want to store this password in a file? (yes/no)")
    print("Your default password storage file is passlist.txt")
    bolne("Your default password storage file is passlist.txt")
    print("Enter your choice:")
    bolne("Enter your choice:")
    choice = input().strip().lower()
    print("What name do you want to store  this password as:")
    bolne("What name do you want to store this password as:")
    name_pass = sunne().strip()
    store=f"{name_pass}: {password}"
   
    if choice == 'yes':
        with open("passlist.txt", "a") as file:
            file.write(store+"\n")
        print("Password stored in password.txt")
        bolne("Password stored in password.txt")
    else:
        print("Password not stored.")
        bolne("Password not stored.")

if __name__ == "__main__":
    generator()
   
