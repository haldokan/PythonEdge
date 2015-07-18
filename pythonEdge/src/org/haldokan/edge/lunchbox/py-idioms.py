#
import sys
from functools import partial
from collections import defaultdict, ChainMap

def iter_with_sentinal():
    f = open('c:/temp/python/baby2008.html.summary')
    blocks = []
    # iter takes a callable (no args) and a sentinal value (''). Since the func
    # f.read(bytes) must not have arg we use partial to wrap the original
    # func and freez its value
    for block in iter(partial(f.read, 16), ''):
        blocks.append(block)
    #we concatenat using join, not +        
    bstr = '#'.join(blocks)
    print(bstr)

def for_with_else(e):
    for i in range(10):
        if i == e: break
    else: return False
    return True

def dict_iter_items():
    dict = {'fn':'Allah', 'pf':'Rab', 'call':'AA'}
    # unlike items, iteritems does not build the whol item list in memory
    for k, v in dict.iteritems():
        print(k, v)

def grouping_with_setdefault():
    names = ['Haytham', 'Bob', 'Rob', 'Khzami', 'Haseba', 'Allah', 'Rabbo']
    # not the arg to the defaultdict here is the func 'list'
    d = defaultdict(list)
    for name in names:
        d[len(name)].append(name)
    print(d)        

def chain_map():
    map1 = dict(a=1, b=2, foo=777)
    map2 = dict(x=11, y=22)
    map3 = dict(foo=111, bar=222, a=3)
    # look up values in all the maps that are in the cmap and return the first
    cmap1 = ChainMap(map1, map2, map3)
    print(cmap1['a'], cmap1['foo'])
    cmap2 = ChainMap(map3, map2, map1)
    print(cmap2['a'], cmap2['foo'])
    
def main():
    #iter_with_sentinal()
    #print(for_with_else(5))
    #print(for_with_else(15))
    #dict_iter_items()
    #grouping_with_setdefault()
    chain_map()

if __name__ == '__main__':
    main()


