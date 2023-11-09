from openai import OpenAI
import json

class Bot:
    def __init__(self):
        self.client = OpenAI()
        self.model="gpt-3.5-turbo"
        self.messages = messages=[
            {"role": "system", "content": "Du bist ein Home-Automations Assistent. Du bekommst einen Befehl von einem Benutzer und sollst diesen in einen Funktionsaufruf umwandeln."},
        ]
        self.tools = []
        self.available_functions = {}

    def add_tool(self, tool_desc, func):
        self.tools.append(tool_desc)
        self.available_functions[tool_desc["function"]["name"]] = func
        
    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def run(self):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            tools=self.tools,
            tool_choice="auto",  # auto is default, but we'll be explicit
        )

        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = self.available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                light_id=function_args.get("light_id"),
                status=function_args.get("status"),
            )

        return response_message