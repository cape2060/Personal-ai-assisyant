import hashlib
import pyttsx3

def bolne(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Changing voice
    engine.say(text)
    engine.runAndWait()




def hash_type(hash):
    if len(hash)==32:
        print("This is an MD5 hash")
        bolne("This is an MD5 hash")
        return 1
    elif len(hash)==40:
        print("This is a SHA1 hash")
        bolne("This is a SHA1 hash")
        return 2
    elif len(hash)==64:
        print("This is a SHA256 hash")
        bolne("This is a SHA256 hash")
        return 3
    elif len(hash)==128:
        print("This is a SHA512 hash")
        bolne("This is a SHA512 hash")
        return 4
    elif len(hash)==56:
        print("This is a SHA224 hash")
        bolne("This is a SHA224 hash")
        return 5
    elif len(hash)==96:
        print("This is a SHA384 hash")
        bolne("This is a SHA384 hash")
        return 6
    elif '$' in hash:
        print("This is a bcrypt hash")
        bolne("This is a bcrypt hash")
        print("It is difficult to crack because it is slow and the hash changes every time we create but can be done usinf checkpasswd in bcrypt but only work in weak password")
        bolne("It is difficult to crack because it is slow and the hash changes every time we create but can be done using checkpasswd in bcrypt but only works in weak passwords")


    else:
        print("Till now i do not know the hash type")
        bolne("Till now I do not know the hash type")



def md5_hashchecker(list,hash):
    with open(list, "r") as file:
        for line in file:
            word = line.strip()
            hashed = hashlib.md5(word.encode()).hexdigest()
            
            if hashed == hash:
                print(f"[+] Hash cracked! The word is: {word}")
                bolne(f"Hash cracked! The word is: {word}")
                break
            else:
                print(f"[-] {word} does not match the hash.")
                
                continue

def sha1_hashchecker(list,hash):
    with open(list, "r") as file:
        for line in file:
            word = line.strip()
            hashed = hashlib.sha1(word.encode()).hexdigest()
            if word =="":
                print("The word is empty, skipping...")
                bolne("The word is empty, skipping...")
                exit()
                        
            if hashed == hash:
                print(f"[+] Hash cracked! The word is: {word}")
                bolne(f"Hash cracked! The word is: {word}")
                break
            else:
                print(f"[-] {word} does not match the hash.")
                
                continue

def sha224_hashchecker(list,hash):
    with open(list, "r") as file:
        for line in file:
            word = line.strip()
            hashed = hashlib.sha224(word.encode()).hexdigest()
            
            if hashed == hash:
                print(f"[+] Hash cracked! The word is: {word}")
                bolne(f"Hash cracked! The word is: {word}")
                break
            else:
                print(f"[-] {word} does not match the hash.")
                
                continue

def sha256_hashchecker(list,hash):
    with open(list, "r") as file:
        for line in file:
            word = line.strip()
            hashed = hashlib.sha256(word.encode()).hexdigest()
            
            if hashed == hash:
                print(f"[+] Hash cracked! The word is: {word}")
                bolne(f"Hash cracked! The word is: {word}")
                break
            else:
                print(f"[-] {word} does not match the hash.")
                
                continue

def sha384_hashchecker(list,hash):
    with open(list, "r") as file:
        for line in file:
            word = line.strip()
            hashed = hashlib.sha384(word.encode()).hexdigest()
            
            if hashed == hash:
                print(f"[+] Hash cracked! The word is: {word}")
                bolne(f"Hash cracked! The word is: {word}")
                break
            else:
                print(f"[-] {word} does not match the hash.")
                
                continue

def sha512_hashchecker(list,hash):
    with open(list, "r") as file:
        for line in file:
            word = line.strip()
            hashed = hashlib.sha512(word.encode()).hexdigest()
            
            if hashed == hash:
                print(f"[+] Hash cracked! The word is: {word}")
                bolne(f"Hash cracked! The word is: {word}")
                break
            else:
                print(f"[-] {word} does not match the hash.")
                    
                continue


def main():
    print("Welcome to the Hash Cracker!")
    bolne("Welcome to the Hash Cracker!")
    print("ENter the hash you want to crack:")
    bolne("Enter the hash you want to crack:")
    hash=input()
    
    bolne("Checking hash type...")
    integer=hash_type(hash)
   
    print("Do you want to crack the hash (yes/no)")
    bolne("Do you want to crack the hash yes or no")
    answer=input().strip().lower()
    if answer == "yes":
        print("Please provide the path to your custom wordlist:")
        bolne("Please provide the path to your custom wordlist:")
        list = input()
    
    else:
        exit()
    
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

if __name__=="__main__":
    main()