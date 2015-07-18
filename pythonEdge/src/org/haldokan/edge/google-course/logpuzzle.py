#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
from urllib import request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  # GET /foo/talks/
  # GET /edu/languages/google-python-class/images/puzzle/a-baaj.jpg
  urls = []
  file = open(filename, 'rU')
  server = filename[filename.index('_') + 1:]
  for line in file:
    match = re.search(r'GET(\s+)(\S+)', line)
    if match and 'puzzle' in line:
      #matchstr = match.group()      
      #urls.append('http://' + server + matchstr[matchstr.index('/'):])
      # use group(2)
      urls.append('http://' + server + match.group(2))
  
  urlset = {}.fromkeys(urls)
  return sorted(urlset.keys(), key=sortkey)       

def sortkey(url):
  #-wordchars-wordchars.jpg
  # the brackets (\w+) signifies matching gropus starting at 1. So we can call
  # match.group(1), or match.group(2), etc. match.group(0) give the whole match
  # similar to match.group()
  match = re.search(r'-(\w+)-(\w+).jpg', url)
  if match and url.endswith(match.group()):
    # return url[url.rindex('-') + 1:url.rindex('.')]
    return match.group(2)
  else: return url

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
  img_count = 0
  img_names = []
  for url in img_urls:
    try:
      print('Getting image from url: ' + url)
      urlfile = request.urlopen(url)
      img = urlfile.read()
      urlfile.close()
      img_name = 'img' + str(img_count)
      img_names.append(img_name)
      file = open(os.path.join(dest_dir, img_name), 'wb')
      img_count += 1
      file.write(img)
      file.close()
    except IOError as err:
      print('problem reading url: %s, exception: %s' % (url, err))  
  make_index_file(img_names, dest_dir)

def make_index_file(img_names, dest_dir):
  index_file = '<verbatim>\n<html>\n<body>\n'
  for img_name in img_names:
    path = os.path.abspath(os.path.join(dest_dir, img_name))
    index_file += '<img src="' + path + '">'
  index_file += '\n</body>\n</html>\n'  

  file = open(os.path.join(dest_dir, 'index.html'), 'w')
  file.write(index_file)
  file.close()

def download_images2(urls, dest):
  if not os.path.exists(dest): os.makedirs(dest)
  index = open(os.path.join(dest, 'index.html'), 'w')
  index.write('<verbatim>\n<html>\n<body>\n')

  count = 0
  for url in urls:
    local_name = 'img%d' % count
    print('Retrieving....%s' % url)
    index.write('<img src="%s">' % os.path.join(dest, local_name))
    # the urlretrieve is ported form python 2 and considered legacy that will
    # be removed in the future. The way I did download_images in the other func
    # is the right way. Check the urllib.request for many other way a file can
    # be read and deconded, etc.
    request.urlretrieve(url, os.path.join(dest, local_name))
    count += 1

  index.write('\n</body>\n</html>\n')
  index.close()
                
    
def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
 
  img_urls = read_urls(args[0])

  if todir:
    #download_images(img_urls, todir)
    download_images2(img_urls, todir)
    
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
