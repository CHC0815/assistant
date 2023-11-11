import configparser
import time

class Context:
    def __init__(self, role, content, timestamp=None):
        self.role = role or ""
        self.content = content or ""
        self.timestamp = timestamp or time.time()

class ContextQueue:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")

        self.timeout = (int(config["Assistant"]["context_timeout"]) or 5) * 60
        self.amount = int(config["Assistant"]["context_amount"]) or 10

        self.queue: list[Context] = []


    def add(self, context: Context):
        self.queue.append(context)

    def get(self) -> list[Context]:
        # Remove expired contexts
        self.queue = [c for c in self.queue if c.timestamp + self.timeout > time.time()]
        # use omly the last n contexts
        self.queue = self.queue[-self.amount:]
        return self.queue