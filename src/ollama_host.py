import ollama

class ollama_host:

    def __init__(self, ollama_host: str, ollama_port: int):
        self.host = ollama_host
        self.port = ollama_port

        
        self.socket = server_socket("127.0.0.1", 1630)


    def parse(self) -> str:
        # configured for functionality
        pass

    def send(self):
        # parse and send data
        pass

    def start(self):
        connection = self.socket.listen()
        # start recieving and parsing requests here


    
    
