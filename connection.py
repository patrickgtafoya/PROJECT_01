import socket
import sys


class Server:
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 5100
        print(self.ip)
        # socket
        self.s = socket.socket()
        self.s.bind(('', self.port))
        print(self.s.getsockname())
        self.s.listen()

    def close_socket(self):
        self.s.close()

    def establish_connection(self):
        while True:
            c, addr = self.s.accept()
            print('got connection from: ', addr)
            c.send('connected'.encode())


class Client:
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        print(self.ip)
        self.server = ['10.0.0.27', 5100]
        # socket
        self.s = socket.socket()

    def close_socket(self):
        self.s.close()

    def establish_connection(self):
        self.s.connect((self.server[0], self.server[1]))
        recv = self.s.recv(1024).decode()
        print(recv)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('to run:\nconnection.py [arg]\n[arg] server or client')
        sys.exit()
    if sys.argv[1] == 'server':
        server = Server()
        server.close()
    elif sys.argv[1] == 'client':
        client = Client()
        client.close_socket()
    else:
        print('to run:\nconnection.py [arg]\n[arg] server or client')
        sys.exit()
