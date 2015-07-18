#
import socketserver
import socket
import threading
import sys

class ThreadedTcpHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.data = str(self.rfile.readline().strip(), 'utf-8')
        currthread = threading.current_thread()
        self.wfile.write(bytes('{}.{}'.format(currthread.name, self.data.upper()), 'utf-8'))
        
class ThreadedTcpServer(socketserver.ThreadingMixIn, socketserver.TCPServer): pass

def client(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(('localhost', 7777))
        sock.sendall(bytes(data + '\n', 'utf-8'))
        received = str(sock.recv(1024), 'utf-8')
    finally:
        sock.close()
        print('client sends {}'.format(data))
        print('client receives {}'.format(received))
    
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        raise RuntimeError('at least one arg should be defined')
    option = args[0]
    if option == '--server':
        host, port = 'localhost', 7777

        sockserver = ThreadedTcpServer((host, port), ThreadedTcpHandler)
        server_thread = threading.Thread(target=sockserver.serve_forever)
        server_thread.daemon = True
        server_thread.start()
     
        print('ThreadedTCPServer is running in thread %s ...' % server_thread.name)

        client(" ".join(args[1:]))

        sockserver.shutdown()
        
    else: raise RuntimeError('option %s is not defined' % option)

if __name__ == '__main__':
    main()
