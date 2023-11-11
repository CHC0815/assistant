from pydub import AudioSegment
from pydub.playback import play
import configparser

def play_beep():
    config = configparser.ConfigParser()
    config.read("config.ini")
    noise = AudioSegment.from_wav("./assets/beep.wav")
    noise = noise + config["Assistant"]["volume"]
    print('beep')
    play(noise)

if __name__ == "__main__":
    play_beep()