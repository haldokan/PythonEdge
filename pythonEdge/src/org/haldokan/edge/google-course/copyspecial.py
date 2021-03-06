#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dirname):
  files = os.listdir(dirname)
  sfiles = []
  for file in files:
    if re.search(r'__(\w+)__',file):
      sfiles.append(os.path.abspath(os.path.join(dirname, file)))
  return sfiles

def copy_to(paths, destdir):
  if not os.path.exists(destdir):
    # similar to linux mkdir -p mydir
    os.makedirs(destdir)
  for file in paths:
    fname = os.path.basename(file)
    shutil.copy(file, os.path.join(destdir, fname))

def move(paths, destdir):
  if not os.path.exists(destdir):
    # similar to linux mkdir -p mydir
    os.makedirs(destdir)  
  for file in paths:
    (status, output) = subprocess.getstatusoutput('copy ' + file + ' ' + destdir)
    print('status = ' + str(status))
    print('output  = ' + output)
    if status:
      sys.stderr.write(output)
      sys.exit(1)
    
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for arg in args:
    sfiles = get_special_paths(arg)
    print(sfiles)
    copy_to(sfiles, 'c:\\temp\\python\\sfiles')
  move(sfiles, 'c:\\temp\\python\\sfiles\\archive')
if __name__ == "__main__":
  main()
