#!/usr/bin/python -tt
from collections import deque
import sys
import itertools
import operator

def tail(fname, n=10):
    with open(fname) as f:
        return deque(f, n)

def moving_avg(iterable, n=3):
    itr = iter(iterable)
    deck = deque(itertools.islice(itr, n-1))
    deck.appendleft(0)
    s = sum(deck)
    print('sum = %f' % s)
    for e in itr:
        print('elem = %f' % e)
        s += e - deck.popleft()
        deck.append(e)
        yield s / n

def accum(iterable, func=operator.sub):
    itr = iter(iterable)
    accumulate = next(itr)
    yield accumulate
    for e in itr:
        accumulate = func(accumulate, e)
        yield accumulate
    
def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print('Usage experiment func_name')
        sys.exit(1)
        
    func = args[0]
    if func == 'tail':
        print(tail('c:\\temp\\mfile.txt'))
    elif func == 'moving_avg':
        l = [1.3, 1.4, 2.9, 44.934, 51.343, 77.343, 8343.843, 9343.343, 1.5, 99.99]
        iterable = moving_avg(l, 3)
        for e in iterable:
            print(e)
    elif func == 'accum':
        iterable = accum([1,2,3,4,5,6,7,8,9,10])
        for e in iterable: print(e)

        accum_list = list(accum([1,2,3,4,5,6,7,8,9,10], operator.add))
        print(accum_list)

        accum_list = list(accum([1,2,3,4,5,6,7,8,9,10], lambda n1, n2: n1 * n2))
        print(accum_list)
    else: raise RuntimeError('function %s is not defined' % func)
    

##
if __name__ == '__main__':
    main()
