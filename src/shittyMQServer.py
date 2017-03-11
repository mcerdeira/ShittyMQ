import sys
import socket
from threading import *

messageQueue = []
subscribers = []

class Client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            m = self.sock.recv(1024).decode()
            messageQueue.append(m)
            if subscribers.__len__() > 0:
                

def _main(argv):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    shost = socket.gethostname()
    sport = 8000
    server_socket.bind((shost, sport))
    server_socket.listen()
    
    subs_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8100
    subs_socket.bind((host, port))
    subs_socket.listen()
    
    print ('Listening on %s:%d' % (shost, sport))
    print ('Subscribers on %s:%d' % (host, port))
    while 1:
        # Get Subscribers
        sub_socket, sub_address = subs_socket.accept()
        subscribers.append(subscribers)
        # Accept client messages
        clientsocket, address = server_socket.accept()
        Client(clientsocket, address)
    
if __name__ == '__main__':
    _main(sys.argv)