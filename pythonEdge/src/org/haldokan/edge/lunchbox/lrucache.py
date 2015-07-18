#!/usr/bin/python -tt
from collections import deque
import sys
import itertools
import operator
import urllib
from urllib import request
from urllib import error
from functools import lru_cache

# maxsize is better when pow of 2
@lru_cache(maxsize=32)
def get_pep(num):
    try:
        rsrc = 'http://www.python.org/dev/peps/pep-%04d/' % num
        with urllib.request.urlopen(rsrc) as url_rsrc:
            return url_rsrc.read()
            
    except urllib.error.HTTPError:
        return 'NOT FOUND'

    
def main():
    args = sys.argv[1:]
    for num in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
        print(num, get_pep(num))

    print(get_pep.cache_info())        
##
if __name__ == '__main__':
    main()
