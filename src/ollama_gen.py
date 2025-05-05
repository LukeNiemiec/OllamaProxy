# TODO: 
#   . install and run ollama


# SOURCE: https://github.com/ollama/ollama-python
# chats have a model and tools at their disposal
from ollama import Client, ChatResponse, embed

# capabilities:
#   . message history       
#   . saving states to come back to it later                        -> pickle / file io
#   . new models can be specified as a branch from a regular model  -> https://github.com/ollama/ollama-python/blob/main/examples/create.py
#   . output formating                                              -> https://github.com/ollama/ollama-python/blob/main/examples/structured-outputs.py
#   . support for models:
#       . qwen2.5-coder:0.5b					
#       . llama2-uncensored:7b
#       . deepseek-r1:8b						d
#       . qwen2-math:1.5b						
#       . llama3.2:1b							
#       . granite3.2:8b							


# model files: https://github.com/ollama/ollama/blob/main/docs/modelfile.md

# workflow:
#   . ask what task I am trying to accomplish and forward to a specialized agent
#   . 

response = embed(model='jeffh/intfloat-multilingual-e5-large-instruct:f16', input="""your purpose is to categorize prompts into any of the following categories:
	 MATH: for a prompt that is asking a question that requires math to solve,
	 CODING: for a prompt that is asking a question that requires coding knowledge to answer
	 ILLEGAL: for a prompt that requires knowledge of illegal topics to elaborate or answer
	 GENERAL: for a prompt that cant be categorized as either MATH, CODING, or ILLEGAL
""")


print(response)


class cchat:
    def __init__(self, server_port):

        self.client = Client(
            host = f"http://localhost:{server_port}"
        )

        # contains a list of previous messages from this session
        self.messages = []

# 
#     def start_chat(self):
# 
#         self.messages = [{
#             'role': 'user',
#             'content': f'Categorize the prompt: "{input(": ")}"'
#         }]
# 
# 
#         categorize_prompt = {
#           'type': 'function',
#           'function': {
#             'name': 'categorize_prompt',
#             'description': 'categorize the prompt as only one of the following: "Math", "Code", "Illegal", "General";',
#             'parameters': {
#               'type': 'object',
#               'required': ['task', 'category'],
#               'properties': {
#                 'task': {'type': 'string', 'description':'The task that the user is prompting about.'}
#                 'category': {'type': 'string', 'description': 'A category to put the prompt into: "Math", "Writing", "Text Analysis", "Programming", "Illegal", "General"'},
#               },
#             },
#           },
#         }
#         
#         response: ChatResponse = self.client.chat(
#             model = "qwen2.5:0.5b",
#             messages = self.messages,
#             tools=[categorize_prompt],
#             options = {'temperature': 0},
#         )
# 
# 
#         print(response)

# if __name__ == "__main__":
#     c = cchat(11434)
#     c.start_chat()
