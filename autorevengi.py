import angr
import pyttsx3
import time

def bolne(text):
    engine= pyttsx3.init()
    engine.getProperty('voices')
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.say(text)
    engine.runAndWait()


def check(path,correct):
    start_time=time.time()
    try:
        project =angr.Project(path)
    except Exception as e:
        print("\033[91mError loading the binary:", e)
        bolne("Error loading the binary: " + str(e))
        return
    entry = project.factory.entry_state()
    manager = project.factory.simulation_manager(entry)
    manager.explore(find=correct)
    if manager.found:
        found = manager.found[0]
        print("\033[92mKey found:", found.posix.dumps(0).decode().strip())
        bolne("Key found: " + found.posix.dumps(0).decode().strip())
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\033[92mTime taken to find the key: {elapsed_time:.2f} seconds")
        bolne(f"Time taken to find the key: {elapsed_time:.2f}seconds")
    else:
        print("No solution found.")

def check1(path,address):
    start_time = time.time()
    try:
        project =angr.Project(path)
    except Exception as e:
        print("\033[91mError loading the binary:", e)
        bolne("Error loading the binary: " + str(e))
        return
    entry = project.factory.entry_state()
    manager = project.factory.simulation_manager(entry)
    manager.explore(find=address)
    if manager.found:
        found = manager.found[0]
        print("\033[92mKey found:", found.posix.dumps(0).decode().strip())
        bolne("Key found: " + found.posix.dumps(0).decode().strip())
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\033[92mTime taken to find the key: {elapsed_time:.2f} seconds")
        bolne(f"Time taken to find the key: {elapsed_time:.2f} seconds")
    else:
        print("\033[92mNo solution found.")
        bolne("No solution found.")

def main():
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

if __name__ == "__main__":
    main()  

        
