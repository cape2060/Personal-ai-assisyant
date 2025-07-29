import pyttsx3
import winsound

import time

DOT_DURATION = 150  # milliseconds
DASH_DURATION = 400
FREQUENCY = 750  # hz
GAP = 0.3#second

def play(code):
    for char in code:
        if char == '.':
            winsound.Beep(FREQUENCY, DOT_DURATION)
            time.sleep(GAP)
        elif char == '-':
            winsound.Beep(FREQUENCY, DASH_DURATION)
            time.sleep(GAP)
        elif char == ' ':
            time.sleep(GAP * 2)  # gap between letters
        elif char == '/':
            time.sleep(GAP * 4)  # gap between words

engine = pyttsx3.init()
def bolne(text):
    
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)  # Set to the first
    engine.say(text)
    engine.runAndWait()

def decoder(code):
    if code == '.-':
        return 'A'
    
    elif code == '-...':
        return 'B'
    elif code == '-.-.':
        return 'C'
    elif code == '-..':
        return 'D'
    elif code == '.':
        return 'E'
    elif code == '..-.':
        return 'F'
    elif code == '--.':
        return 'G'
    elif code == '....':
        return 'H'
    elif code == '..':
        return 'I'
    elif code == '.---':
        return 'J'
    elif code == '-.-':
        return 'K'
    elif code == '.-..':
        return 'L'
    elif code == '--':
        return 'M'
    elif code == '-.':
        return 'N'
    elif code == '---':
        return 'O'
    elif code == '.--.':
        return 'P'
    elif code == '--.-':
        return 'Q'
    elif code == '.-.':
        return 'R'
    elif code == '...':
        return 'S'
    elif code == '-':
        return 'T'
    elif code == '..-':
        return 'U'
    elif code == '...-':
        return 'V'
    elif code == '.--':
        return 'W'
    elif code == '-..-':
        return 'X'
    elif code == '-.--':
        return 'Y'
    elif code == '--..':
        return 'Z'
    else:
        return ''

def encoder(code):
    
    if code == 'A' or code == 'a':
        return '.-'
    elif code == 'B' or code == 'b':
        return '-...'
    elif code == 'C' or code == 'c':
        return '-.-.'
    elif code == 'D' or code == 'd':
        return '-..'
    elif code == 'E' or code == 'e':
        return '.'
    elif code == 'F' or code == 'f':
        return '..-.'
    elif code == 'G' or code == 'g':
        return '--.'
    elif code == 'H' or code == 'h':
        return '....'
    elif code == 'I' or code == 'i':
        return '..'
    elif code == 'J' or code == 'j':
        return '.---'
    elif code == 'K' or code == 'k':
        return '-.-'
    elif code == 'L' or code == 'l':
        return '.-..'
    elif code == 'M' or code == 'm':
        return '--'
    elif code == 'N' or code == 'n':
        return '-.'
    elif code == 'O' or code == 'o':
        return '---'
    elif code == 'P' or code == 'p':
        return '.--.'
    elif code == 'Q' or code == 'q':
        return '--.-'
    elif code == 'R' or code == 'r':
        return '.-.'
    elif code == 'S' or code == 's':
        return '...'
    elif code == 'T' or code == 't':
        return '-'
    elif code == 'U' or code == 'u':
        return '..-'
    elif code == 'V' or code == 'v':
        return '...-'
    elif code == 'W' or code == 'w':
        return '.--'
    elif code == 'X' or code == 'x':
        return '-..-'
    elif code == 'Y' or code == 'y':
        return '-.--'
    elif code == 'Z' or code == 'z':
        return '--..'
      
    else:
        return ''

def seperator1(sen):
    length=len(sen)
    word=''
    for i in range(0,length):
        if sen[i] == ' ':
            word+='/'
        
        word+=encoder(sen[i])
        word=word+' '
    print(f"Output of sentense '{sen}' is {word+' /'.strip()}")
    bolne(f"Output of sentence {sen} in morse code is ")
    play(word)


def seperator(code):
    length=len(code)
    ball=''
    word=''
    for i in range(0,length):
        if code[i]=='/':
            word=word+' '
            ball=''
        elif code[i]==' ':
            
            
            word+=decoder(ball)
            
            
            ball=''
            
        else:
            ball+=code[i]
    
    print(word)
    bolne(f"Output of morse code  is {word}")

def main():
    print("ENter what you want sentence to morse code  or morse code to sentence (stm/mts):")
    bolne("Enter what you want sentence to morse code or morse code to sentence (stm/mts):")
    choice=input().lower().strip()
    if choice == 'stm':
        print("Enter the sentence:")
        bolne("Enter the sentence:")
        sen=input()
        seperator1(sen)
        
    elif choice == 'mts':
        print("Enter the morse code each word seperated by '/' (eg: .. / .. /):")
        bolne("Enter the morse code each word seperated by '/' (example: .. / .. /):")
        code=input()
        
        seperator(code)
    
if __name__=="__main__":
    main()