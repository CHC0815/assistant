from pydub import AudioSegment
from pydub.playback import play


def play_beep():
    noise = AudioSegment.from_wav("./assets/beep.wav")
    print('beep')
    play(noise)

if __name__ == "__main__":
    play_beep()