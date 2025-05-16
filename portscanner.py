import socket
import speech_recognition as sr
import pyttsx3

listener=sr.Recognizer()

def bolne(text):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Changing voice
    engine.say(text)
    engine.runAndWait()

def sunne():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            print("You:", command)
            return command
    except Exception as e:
        print(f"Error occured:{e}")
        bolne(f"Error occured:{e}")
def scanner(target_ip, starting,ending):
    portlist=[]
    for port in range(int(starting),int(ending)+1):
        try:
            
            print(f"Scanning {target_ip} on port {port}...")
            
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            
            result = sock.connect_ex((target_ip, int(port)))
            if result == 0:
                print(f"Port {port} is open.")
                bolne(f"Port {port} is open.")
                portlist.append(port)
            else:
                print(f"Port {port} is closed.")
             
           
            sock.close()
        except Exception as e:
            print(f"Error: {e}")
            bolne(f"Error: {e}") 
    print(f"Open ports are: {portlist}") 
    bolne(f"Open ports are: {portlist}")    
def checking(target):
    try:
        socket.gethostbyname(target)    
        return True
    except Exception as e:
        return False   



def main():
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
    

    print("Enter the port you wabt yo scan from 1 to 65535")
    bolne("Enter the port you wabt yo scan from 1 to 65535(starting port)")
    starting=sunne()
    print("Enter the port you wabt yo scan from 1 to 65535")
    bolne("Enter the port you wabt yo scan from 1 to 65535(ending port)")
    ending=sunne()
    scanner(target, starting, ending)
    print("Scanning completed.")
    bolne("Scanning completed.")


if __name__=="__main__":
    main()


