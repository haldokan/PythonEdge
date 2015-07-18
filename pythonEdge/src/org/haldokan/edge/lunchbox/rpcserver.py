#
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc import client
import sys

class TestRequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class TestRPCClass():
    def mult(self, x, y):
        return x * y
    
    def div(self, x, y):
        return x / y

def adder_func(x, y):
    return x + y

def rpcserver():
    server = SimpleXMLRPCServer(('localhost', 8000), requestHandler=TestRequestHandler)
    server.register_introspection_functions()
    server.register_function(pow)
    server.register_function(adder_func, 'add')
    server.register_instance(TestRPCClass())

    server.serve_forever()

def rpcclient():
    proxy = client.ServerProxy('http://localhost:8000')
    print(proxy.pow(2,3))
    print(proxy.add(2,3))
    print(proxy.mult(2,3))
    print(proxy.div(2,3))
    print(proxy.system.listMethods())

def main():
    args = sys.argv[1:]
    option = args[0]
    if option == '--server':
        rpcserver()
    elif option == '--client':
        rpcclient()
    else:
        raise RuntimeError('option %s is not defined' % option)

if __name__ == '__main__':
    main()
