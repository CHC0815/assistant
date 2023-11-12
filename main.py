from recognizer import Recognizer
from tools.set_light_status import SET_LIGHT_STATUS
from bot import Bot
import configparser
from sound import play_beep
from context_queue import ContextQueue, Context
from speak import speak

def main():
    config = configparser.ConfigParser()
    config.read("config.ini")
    rec = Recognizer()
    tool = SET_LIGHT_STATUS
    c_queue = ContextQueue()

    while True:
        name = config["Assistant"]["Name"] or "bob"
        answer = bool(config["Assistant"]["Answer"] or False)
        rec.listen(trigger=name or "bob")
        play_beep()
        bot = Bot()
        bot.add_context_queue(c_queue)

        promt = rec.listen()["transcription"]
        print(f"Prompt: {promt}")
        bot.add_tool(tool)
        bot.add_message("user", promt)
        c_queue.add(Context("user", promt))

        response = bot.run()
        if answer:
            speak(response.content)
        print(f"Response: {response}")


if __name__ == "__main__":
    main()