# load the large language model file
from llama_cpp import Llama
LLM = Llama(model_path="/Users/mac04/Downloads/llama-2-7b-chat.ggmlv3.q8_0.bin")

# create a text prompt
prompt = "Answer as function call in the form of a string with the pattern: 'set_light_level(id, state)'. Q: Please set the nightlight to 50%."

# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])