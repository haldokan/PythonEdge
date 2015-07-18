#
import socketserver
import socket
import sys

class TestTcpHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline().strip()
        print("{} write ".format(self.client_address[0]))
        print(self.data)
        self.wfile.write(self.data.upper())

def serverclient(data):        
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(('localhost', 7777))
        sock.sendall(bytes(data + '\n', 'utf-8'))
        received = str(sock.recv(1024), 'utf-8')
    finally:
        sock.close()
    print('client sends: {}'.format(data))        
    print('client receives: {}'.format(received))
    
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        raise RuntimeError('at least one arg should be defined')
    option = args[0]
    if option == '--server':
        host, port = 'localhost', 7777
        sockserver = socketserver.TCPServer((host, port), TestTcpHandler)
        print('TCPServer is running...')
        sockserver.serve_forever()
    elif option == '--client':
        serverclient(" ".join(args[1:]))
        
    else: raise RuntimeError('option %s is not defined' % option)

if __name__ == '__main__':
    main()    
              
        
                     
