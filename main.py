from recognizer import Recognizer
from assistant import get_tool_set_light_status
from bot import Bot

def main():
    rec = Recognizer()
    tool = get_tool_set_light_status()
    bot = Bot()
    
    promt = rec.listen()["transcription"]
    print(f"Prompt: {promt}")
    bot.add_tool(tool[0], tool[1])
    bot.add_message("user", promt)

    print(bot.run())


if __name__ == "__main__":
    main()