import configparser
from bot import Bot
from context_queue import Context, ContextQueue
from recognizer import Recognizer
from sound import play_beep
from speak import speak
from tools.set_light_status import SET_LIGHT_STATUS
from cmd_parser import parse_cmd

class App:
    def __init__(self, config_path: str = "config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self.rec = Recognizer()
        self.tool = SET_LIGHT_STATUS
        self.c_queue = ContextQueue()
        self.answer = bool(self.config["Assistant"]["Answer"] or False)
        self.name = self.config["Assistant"]["Name"] or "bob"


    def get_prompt(self) -> str:
        promt = self.rec.listen()["transcription"]
        print(f"Prompt: {promt}")

    def wait_for_activation(self):
        self.rec.listen(trigger=self.name)

    def run(self):
        while True:
            self.wait_for_activation()
            play_beep()
            promt = self.get_prompt()

            id, state, success = parse_cmd(promt)
            if success:
                self.tool.set_light_status(id, state)
                continue

            bot = Bot().add_context_queue(self.c_queue).add_tool(self.tool)
            bot.add_message("user", promt)
            self.c_queue.add(Context("user", promt))

            response = bot.run()
            if self.answer:
                speak(response.content)
            print(f"Response: {response}")