import socket as s


class SendException(Exception):
    def __init__(self, message):
        super(self, f"Error sending: {message}")

class ParseException(Exception):
    def __init__(self, command):
        super(self, f"Error parsing command: {command}")

class client_socket:
    def __init__(self):
        self.socket = s.socket()


    def connect(self, host: str, port: int):
        self.socket.connect((host, port))


    def parse(self, command):


        # raise ParseException()


    def send(self, data)
        data

    def close(self):
        self.socket.close()
