#!C:\haldokan\3p\Python34\python.exe -u

import sys
from multiprocessing import Pool, Process, Queue, Pipe, Lock, Manager
import os

def somefunc(x): return x*x

def info(title):
    print(title)
    print('modname: ', __name__)
    print('ppid: ', os.getppid())
    print('pid: ', os.getpid())

def somefunc2(name):
    info('somefunc2')
    print('hello', name)

def somefunc3(qu):
    qu.put(['foo','bar','baz'])

def somefunc4(pipe):
    pipe.send('hello foo, how are you?')

def somefunc5(lock, num):
    lock.acquire()
    try:
        print(num)
    finally:
        lock.release()

def somefunc6(ddict, llist):
    ddict['name'] = 'Haytham'
    ddict['profession'] = 'Allah'
    ddict['salary'] = 77.11
    llist.reverse()
    
def main():
    args = sys.argv[1:]

    option = args[0]
    if option == '--process1':
        with Pool(5) as p:
            print(p.map(somefunc, [1, 2, 3]))
    elif option == '--process2':
        info('->main')
        p = Process(target=somefunc2, args=('bob',))
        p.start()
        p.join()
    elif option == '--process3':
        qu = Queue()
        p = Process(target=somefunc3, args=(qu,))
        p.start()
        print(qu.get())
        p.join()
    elif option == '--process4':
        end1, end2 = Pipe()
        p = Process(target=somefunc4, args=(end1,))
        p.start()
        print(end2.recv())
        p.join()
    elif option == '--process5':
        lock = Lock()
        for i in range(10):
            Process(target=somefunc5, args=(lock, i)).start()
    elif option == '--process6':
        with Manager() as m:
            m = Manager()
            l = m.list(range(10))
            d = m.dict()
            p = Process(target=somefunc6, args=(d, l))
            p.start()
            p.joint()
            print(d)
            print(l)
        
if __name__ == '__main__':
    main()
