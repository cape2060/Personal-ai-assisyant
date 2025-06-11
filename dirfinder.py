import requests
from subdomain import bolne
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor as tpe
import threading
import subprocess

ok_200 = []
forbidden_403 = []
lock = threading.Lock()

# def info_url():
#     print("Enter the target url")
#     bolne("Enter the target url")
#     url=input().strip()

# info_url()

def wordset(url, dir):
   
    with open(dir, "r") as file:
        words = [word.strip() for word in file if word.strip()]  # Clean and skip empty lines

            
            
    with tpe(max_workers=10) as executor:
        for word in words:
            executor.submit(find_directory,url,word)

def find_directory(url, word):
    try:    
        
        url1=f"{url}/{word}"
        response=requests.get(url1,headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            print(Fore.GREEN + f"[+] Directory found: {word}" + Style.RESET_ALL)           
            bolne(f"Directory found: {word}")
            with lock:    
                ok_200.append(word)
        elif response.status_code == 404:
            print(Fore.BLUE +f"Not found: {word}" + Style.RESET_ALL)   
                    
        elif response.status_code == 403:
            print(Fore.YELLOW + f"[!] Access Forbidden: {word}" + Style.RESET_ALL)   
            with lock:
                forbidden_403.append(word)
        else:
            print(Fore.BLUE+ f"[?] {url1} returned status code {response.status_code}"+ Style.RESET_ALL)
    except requests.RequestException as e:
        print(Fore.RED + f"[!] Error accessing {url1}: {e}" + Style.RESET_ALL)
def bypass403(url):  
    try:
        print("Your choices of attacking are: header, SQLi, protocol, HTTPmethod, encode,port ,for all use exploit.")
        bolne("Your choices of attacking are: header, SQLi, protocol, HTTPmethod, encode,port ,for all use exploit.")
        print("Enter your choice:")
        bolne("Enter your choice:") 
        choice = input().strip()
        # WSL path to your bash script
        script_path = "/mnt/d/Personal-ai-assisyant/bypass.sh"#your bypass.sh script location
        command = f"bash -c \"'{script_path}' -u {url} --{choice}\""

        
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8")

        print("\n[+] Live Script Output:")
        for line in process.stdout:
            print(line, end="")  

        process.wait()  

        if process.returncode != 0:
            print(f"\n[-] Script exited with code {process.returncode}")

    except Exception as e:
        print(f"[!] Error running script: {e}") 
    print(Fore.GREEN + "[+] Bypass end." + Style.RESET_ALL)     
def main():
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

    
if __name__ == "__main__":
     main()
