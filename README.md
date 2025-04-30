# 🧠 Alexa Voice Assistant (Offline + Voice Commands)

A Python-based desktop voice assistant that uses speech recognition, text-to-speech, and local AI (via [Ollama](https://ollama.com/)) to perform tasks like browsing the web, playing YouTube videos, checking the date/time, searching Wikipedia, and interacting with a local LLM like LLaMA 3.

---

## 🚀 Features

- 🎙️ Voice command support (Nepali-accented English: `en-ne`)
- 🔊 Text-to-speech (TTS) with customizable voice
- 🌐 Open websites like YouTube, Facebook, Instagram, etc.
- 📅 Tell current time and date
- 📚 Wikipedia search (short summary)
- 🎵 Play YouTube videos using `pywhatkit`
- 💬 Chat with a local LLM via [Ollama](https://ollama.com/)
- 🧩 Open and close desktop applications (Zoom, browser, etc.)

---

## 🛠️ Installation

### ✅ Requirements

- Python 3.8 or higher
- Microphone (for voice commands)
- Firefox browser installed
- Zoom installed (for `open/close zoom`)
- [Ollama](https://ollama.com/download) installed and running

---

### 📦 Install Dependencies

```bash
pip install pyttsx3 SpeechRecognition wikipedia pywhatkit requests
```

### Optional: If you face errors with pyaudio, install with:
```bash
pip install pipwin
pipwin install pyaudio
```
