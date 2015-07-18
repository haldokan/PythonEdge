#
from concurrent import futures
import traceback

# class that implement __len__ and __getitem__ are iterable
class IterableClass:
    def __init__(self, gods):
        self.gods = gods

    def __len__(self):
        return len(self.gods)

    def __getitem__(self, index):
        # note the len(self) thingy
        if index >= len(self):
            raise IndexError
        return self.gods[index]

    # note that this is func (not method of the class) bcz it has no self arg
    def some_func(arg1, arg2):
        print(arg1, arg2)
    
def extended_unpacking():
    f, *l = range(10)
    print(f, l)

    f, *m, l = ['foo', 'bar', 'baz', 'Allat', 'Rabbo', 'holy cow']
    print(f, m, l)

def big_calc(n):
    return n**100000

def concurr_exec():
    # synchronous
    #l = list(map(lambda n: n**100000, range(20)))
    # concurrent - for some reason we cannot use lambda here
    # does not seem to speed things up tho the presentation indicate a speed
    # factor of 6 times - difference b/w Win & Linux?
    with futures.ProcessPoolExecutor() as ex:
        l = list(ex.map(big_calc, range(20)))
    print(l)

def exception_traceback():
    try:
        raise Exception
    except Exception as ex:
        traceback.print_tb(ex.__traceback__)
def main():
    #extended_unpacking()
    #concurr_exec()
    #exception_traceback()
    god_pantheon = IterableClass(['Allat', 'Rabo', 'Jesus', 'Yahwah',
                                'Buddha', 'Krishna', 'Abou 3abdo'])
    # iterate over class
    for god in god_pantheon:
        print('Holy smoke! He is %s' % god)
    # call the func on the class: use the name of the class...
    # can't use the instance to call a func in the class
    IterableClass.some_func('foo', 'bar')
 
    
if __name__ == '__main__':
    main()
