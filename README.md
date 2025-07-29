# 🧠 Alexa Voice Assistant (Offline + Voice Commands)

A Python-based desktop voice assistant that uses speech recognition, text-to-speech, and local AI (via [Ollama](https://ollama.com/)) to perform tasks like browsing the web, playing YouTube videos, checking the date/time, searching Wikipedia, and interacting with a local LLM like LLaMA 3.It also includes hacking/utility tools like a port scanner, subdomain finder,hash cracking, and background remover.

---

## 🚀 Features

- 🎙️ Voice command support (Nepali-accented English: en-ne)
- 🔊 Text-to-speech (TTS) with customizable voice
- 🌐 Open websites like YouTube, Facebook, Instagram, etc.
- 📅 Tell current time and date
- 📚 Wikipedia search (short summary)
- 🎵 Play YouTube videos using pywhatkit
- 🛡️ Port Scanner (find open ports on any IP/domain)
- 🌐 Subdomain Finder (using DNS brute-force) and Directory Finder — helps bypass 403 errors
- 🔐 Hash Cracker (crack MD5, SHA1, SHA256 using dictionary attack)
- 🖼️ Background Remover (remove image backgrounds)
- 📤 Gmail Sender with Attachment
 - 🔑 Requires SMTP credentials setup (e.g., smtp.gmail.com)
- 🔑 Secure Password Generator (generate strong passwords with voice command, store to file)
- 💬 Chat with a Local LLM via Ollama
- 🧩 Desktop App Control (open/close apps like Zoom, browsers, etc.)
- 🔍 Reverse Engineering Tool using angr
 - 🧠 Automatically finds passwords or keys from binaries with symbolic execution, voice feedback, and result logging
  ---
- 📡 Morse Code Support
 - 🔤 Encode text to Morse (with voice + beep)
 - 🔁 Decode Morse to text (with voice)
 - 🎧 Audio feedback: Dots and dashes played as beeps

---

## 🛠️ Installation

### ✅ Requirements

- Python 3.8 or higher
- Microphone (for voice commands)
- Firefox browser installed
  if not then remove this 3 code line and then put 1 line instead of that 3 and the default browser will run.
  remove:-
  firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
  webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
  webbrowser.get('firefox').open(site[1])
  add:-
  webbrowser.open(site[1])
- Zoom installed (for `open/close zoom`)
  here you can add as many application as you want by adding 2 lines of code for each application.
- [Ollama](https://ollama.com/download) installed and running

---

### 📦 Install Dependencies

```bash
pip install pyttsx3 SpeechRecognition wikipedia pywhatkit requests dnspython rembg angr
```

### Optional: If you face errors with pyaudio, install with:
```bash
pip install pipwin
pipwin install pyaudio
```
### 🧠 Setup Local LLM with Ollama (for AI Chat)
1.Download Ollama: https://ollama.com/download

2.Open a terminal and run:
```bash
ollama pull llama3.2
```
3.Start the server:
```bash
ollama run llama3.2
```
### ▶️  How to Use
1.Clone or download this repo:
```bash
git clone https://github.com/cape2060/Personal-ai-assisyant.git
```
2.Run the assistant:
```bash
python anything.py
```
3.Speak any of the supported commands (listed below). Examples:

-"Open YouTube"

-"Play Despacito"

-"What time is it?"

-"Search Albert Einstein"

-"Open Zoom"

-"subdomain"

-"find directory"

-"scan"

-"cracking hash"

-"Generate password"

-"send email"

-"remove background"

-"reverse engineering"

-"Hello Alexa" → Starts chatting with LLaMA via Ollama
### 🧾 Supported Commands

Voice Command           Example	Description
"Open YouTube"	        Launch YouTube in Firefox
"Play [song name]"	    Play a song/video on YouTube
"Search [topic]"	      Gives a short Wikipedia summary
"What time is it"	      Current time
"What is today’s date"	Current date
"Open Zoom"	            Starts Zoom
"Close Zoom"	          Closes Zoom app
"Close browser"	        Closes Microsoft Edge
"Hello Alexa"         	Starts AI conversation via Ollama
"Exit"	                Exits the assistant

