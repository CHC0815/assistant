from recognizer import Recognizer
from tools.set_light_status import SET_LIGHT_STATUS
from bot import Bot
import configparser
from sound import play_beep

def main():
    config = configparser.ConfigParser()
    config.read("config.ini")
    rec = Recognizer()
    tool = SET_LIGHT_STATUS
    
    while True:
        rec.listen(trigger=config["Assistant"]["Name"])
        play_beep()
        bot = Bot()

        promt = rec.listen()["transcription"]
        print(f"Prompt: {promt}")
        bot.add_tool(tool)
        bot.add_message("user", promt)

        print(bot.run())


if __name__ == "__main__":
    main()