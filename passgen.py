import string
import random
import pyttsx3
def bolne(text):
    
  
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # changing voice
    engine.say(text)
    engine.runAndWait()
def generator():
    firstpart=string.ascii_uppercase
    secondpart=string.ascii_lowercase
    thirdpart=string.digits
    fourthpart=string.punctuation

    total=firstpart+secondpart+thirdpart+fourthpart
    password = ''.join(random.sample(total, 18))
    print(f"Your password is: {password}")
    bolne(f"Your password is: {password}")

if __name__ == "__main__":
    generator()
   