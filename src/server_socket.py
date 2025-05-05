from socket import socket, AF_INET, SOCK_STREAM
from ssl import create_default_context

from subprocess import run
from re import findall, search





class server_socket:
    def __init__(self, start_number = 24, host: str, port: int):

        self.server_address = (host, port) 

        self.encrypt_num = start_number

        self.ssl_context = create_ssl_context()
        
        self.socket = socket(family = AF_INET, type = SOCK_STREAM)

    def parse(self):
        pass
    
    def create_ssl_context(self):
        
        command = [
            "openssl",
            "genpkey",
            "-algorithm", "RSA",
            "-aes256",
            "-out", "my_private_key.pem",
            "-pkeyopt", "rsa_keygen_bits:2048"
        ]


        run(command, input = str(self.encrypt_num))

        print(f"{}")
        
        
        
        
    # close the socket connection
    def close(self):
        self.socket.close()

    #  starts listening for incomming connections
    def get_connection(self):

        with self.ssl_context.wrap_socket() as ssl_:

            self.socket.bind((self.host, self.port))

            self.socket.listen(3)

            return self.socket.accept()

    def send(self, data: str):
        self.socket.send(data.encode())
        self.message_num += 1
         

    def recv(self):
        self.socket.recv()
            
        
