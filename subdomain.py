import dns.resolver
import os
import pyttsx3

def bolne(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def nikalne(filepath):
   
    with open(filepath, 'r') as file:
        w = [line.strip() for line in file if line.strip()]
    return w
def find(domain,wordlist):
    jamma=[]
    for subdomain in wordlist:
        fulldomain=f"{subdomain}.{domain}"
        try:
            dns.resolver.resolve(fulldomain,"A")
            print(f"[-]Subdomain found: {fulldomain}")
            bolne(f"Subdomain found: {fulldomain}")
            jamma.append(fulldomain)
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.LifetimeTimeout):
            pass

        except Exception as e:
            print(f"Error occured:{e}")
            bolne(f"Error occured:{e}")
    return jamma    
def main():
    bolne("Enter the name of domain")
    domain=input("ENter the name of domain:").strip()
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


if __name__=="__main__":
    main()
