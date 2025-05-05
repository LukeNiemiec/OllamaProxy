import ollama

from client_socket import client_socket

class ollama_cli:
    def __init__(self, ollama_host: str, ollama_port: int):
    
        self.host = ollama_host
        self.port = ollama_port
        
        self.socket = client_socket(ip_address, 1630)

    # connects to the ollama server running on LAN
    def connect_ollama():
        pass


    

if __name__ == "__main__":


    cli = ollama_cli(
        "127.0.0.1",         #   ip address of the computer running ollama server
        1630                 #   port of ollama server
    )


