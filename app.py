import configparser
from bot import Bot
from context_queue import Context, ContextQueue
from recognizer import Recognizer
from sound import play_beep
from speak import speak
from tools.set_light_status import SET_LIGHT_STATUS

class App:
    def __init__(self, config_path: str = "config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self.rec = Recognizer()
        self.tool = SET_LIGHT_STATUS
        self.c_queue = ContextQueue()

    def run(self):
        while True:
            name = self.config["Assistant"]["Name"] or "bob"
            answer = bool(self.config["Assistant"]["Answer"] or False)
            self.rec.listen(trigger=name or "bob")
            play_beep()

            promt = self.rec.listen()["transcription"]
            print(f"Prompt: {promt}")

            bot = Bot().add_context_queue(self.c_queue).add_tool(self.tool)
            bot.add_message("user", promt)
            self.c_queue.add(Context("user", promt))

            response = bot.run()
            if answer:
                speak(response.content)
            print(f"Response: {response}")