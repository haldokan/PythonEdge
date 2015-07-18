#
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import datetime
import sys

def today():
    return xmlrpc.client.DateTime(datetime.datetime.today())
def add(x, y):
    return x + y
def sub(x, y):
    return x - y

def read_binary_file():
    with open('c:/temp/python/pageant.exe', 'rb') as reader:
        return xmlrpc.client.Binary(reader.read())
def faulty_add(x, y):
    return x + y + 0j

def rpcserver():
    server = SimpleXMLRPCServer(('localhost',8000))
    print('Listening on port 8000...')
    server.register_multicall_functions()
    server.register_function(today, 'today')
    server.register_function(read_binary_file, 'readbinary')
    server.register_function(faulty_add, 'fadd')
    server.register_function(add)
    server.register_function(sub)
    server.serve_forever()

def rpcclient():
    proxy = xmlrpc.client.ServerProxy('http://localhost:8000')
    today = proxy.today()
    #create date from str
    date = datetime.datetime.strptime(today.value, '%Y%m%dT%H:%M:%S')
    print('Today %s' % date.strftime('%d.%m.%Y, %H:%M'))

    with open('c:/temp/python/pageant-copy.exe', 'wb') as writer:
        #writer.write(proxy.readbinary().data)
        pass
    try:
        proxy.fadd(3, 4)
    except xmlrpc.client.Fault as fault:
        print('fcode %d' % fault.faultCode)
        print('fstr %s' % fault.faultString)

    #url that does not respond to rpc
    proxy2 = xmlrpc.client.ServerProxy('http://google.com/')
    try:
        proxy2.foobar()
    except xmlrpc.client.ProtocolError as perr:
        print('url %s' % perr.url)
        print('errmsg %s' % perr.errmsg)
        print('errcode %d' % perr.errcode)
        print('headers %s' % perr.headers)
        # raise another exception - show how to use traceback
        tb = sys.exc_info()[2]
        raise RuntimeError('encountered protocol error').with_traceback(tb)

    multicall = xmlrpc.client.MultiCall(proxy)
    multicall.today()
    multicall.add(3, 4)
    multicall.sub(3, 4)
    result = multicall();
    print('today=%s, 3 + 4=%d, 3 - 4=%d' % tuple(result))

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
