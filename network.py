import socket

class Network:
    def __init__(self):
        ## Define socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ## Define server details
        self.server = "192.168.1.6"
        self.port = 5555
        self.addr = (self.server, self.port)

        ## Call the connect method on initialization
        self.id = self.connect()
        print(self.id)

    def connect(self):
        ## The client tries to connect to the server using the server address, then listens for a server response
        ## The server script is coded to send "Connected" back to the client, so we decode and assign that above to
        ## self.id
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

n = Network()