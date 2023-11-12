import pyttsx3
from gtts import gTTS
from playsound import playsound

def speak(text: str):
    if text is None:
        return
    tts = gTTS(text, lang='de')
    tts.save('tts.mp3')
    playsound('tts.mp3')

if __name__ == "__main__":
    speak("Hallo Welt")