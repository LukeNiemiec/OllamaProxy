# the purpose of this program is to have a collection of 
# tools that each ollama model has access to essentially 
# creating specialized agents.

class Tools:
    def __init__(self)
        pass

    # EXAMPLE TOOL
    # 
    # categorize_prompt = {
    #   'type': 'function',
    #   'function': {
    #     'name': 'categorize_intention',
    #     'description': 'Using a prompt supplied by the user, categorize the intention of the prompt. The only categories available to you are: Writing, Text Analysis, Math, Coding, Illegal, General',
    #     'parameters': {
    #       'type': 'object',
    #       'required': ['prompt'],
    #       'properties': {
    #         'prompt': {'type': 'string', 'description': 'a question or statement that needs to be categorized'},
    #       },
    #     },
    #   },
    # }

    
# tools in the toolbox are categorized by purpose "name" -> [available functions...]
# ie. if you want tools for generating ideas, name the tools "ideas"

# SOURCE: https://github.com/ollama/ollama-python/blob/8ac9f4da762785e09254271827c7215ca49b20df/examples/tools.py

class Toolbox:
    def __init__(self):
        self.tools = {}

    def addTool(self):
        pass
        # type          ie. function, 
        # name          
        # description   
        # parameters
        
    def getAvailableTools(self, names):
        pass      
