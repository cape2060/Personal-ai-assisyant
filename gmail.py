import smtplib
from email.message import EmailMessage
import mimetypes
import pyttsx3


def bolne(text):
    engine= pyttsx3.init()
    engine.getProperty('voices')
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.say(text)
    engine.runAndWait()
def data():
   
    print("Enter the receiver_email:")#any email can be used
    bolne("Enter the receiver email:")
    receiver_email=input()
    print("Enter the subject:")
    bolne("Enter the subject:")
    subject=input()
    print("Enter email body. Press Enter twice to finish:")
    bolne("Enter email body. Press Enter twice to finish:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    body = "\n".join(lines)

    msg= EmailMessage()
    
    msg["To"]=receiver_email
    msg["Subject"]=subject
    msg.set_content(body)
    print("YOu want to attach an image and a file? (yes/no):")
    bolne("You want to attach an image and a file? (yes/no):")
    attach_choice = input().strip().lower()
    if "y" in attach_choice:

        print("Enter the path of the image to attach:")
        bolne("Enter the path of the image to attach:")
        image_path = input()
        with open(image_path, "rb") as img:
            img_data = img.read()
            maintype, subtype = mimetypes.guess_type(image_path)[0].split('/')
            msg.add_attachment(img_data, maintype=maintype, subtype=subtype, filename="image.jpg")
    print("Do you want to attach a file? (yes/no):")
    bolne("Do you want to attach a file? (yes/no):")
    attach_choice1 = input().strip().lower()
    if "y" in attach_choice1:
        print("Enter the path of the file to attach:")
        bolne("Enter the path of the file to attach:")
        file_path = input()
        print("ENter the file name with extension:")
        bolne("Enter the file name with extension:")
        name = input()
    
        with open(file_path, "rb") as f:
            file_data = f.read()
            maintype, subtype = mimetypes.guess_type(file_path)[0].split('/')
            msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=name)
    print("Sending email...")
    bolne("Sending email...")
    server = "smtp.gmail.com"
    port = 587  
    user = "saitamap66@gmail.com"
    password = "unvr zopi zfkv juke"

    with smtplib.SMTP(server, port) as server:
        server.starttls() 
        server.login(user, password)
        server.send_message(msg)

    print("EMail sent sucessfullly!")
    bolne("Email sent successfully!")
def main():
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


if __name__=="__main__":
    main()





