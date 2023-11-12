from openai import OpenAI
import json
from .context_queue import ContextQueue, Context

class Bot:
    def __init__(self):
        self.client = OpenAI()
        self.model="gpt-3.5-turbo"
        self.messages = messages=[
            {"role": "system", "content": "Du bist ein Home-Automations Assistent. Du bekommst einen Befehl von einem Benutzer und sollst diesen in einen Funktionsaufruf umwandeln."},
        ]
        self.tools = []
        self.available_functions = {}

    def add_tool(self, tool) -> "Bot":
        self.tools.append(tool)
        return self
        
    def add_message(self, role, content) -> "Bot":
        self.messages.append({"role": role, "content": content})
        return self

    def add_context(self, context: Context) -> "Bot":
        self.add_message(context.role, context.content)
        return self

    def add_context_queue(self, context_queue: ContextQueue) -> "Bot":
        for context in context_queue.get():
            self.add_context(context)
        return self

    def run(self):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            tools=list(map(lambda el: el["tool_desc"],self.tools)),
            tool_choice="auto",  # auto is default, but we'll be explicit
        )

        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        if tool_calls is None:
            return response_message

        available_functions = dict(map(lambda el: (el["name"], el["fun"]), self.tools))

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)

            function_params = list(filter(lambda el: el["name"] == function_name, self.tools))[0]["params"]
            args_dict = dict(map(lambda el: (el, function_args.get(el)), function_params))
            function_response = function_to_call(
                **args_dict
            )

        return response_message