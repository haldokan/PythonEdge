#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
from os import listdir
from os.path import isfile, join

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  #year: r'Popularity\sin\s(\d\d\d\d)'
  #names: r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>'
  yearp = re.compile(r'Popularity\sin\s(\d\d\d\d)')
  name_rankp = re.compile(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>')

  rdict = {}
  result = []
  # read the file one line at a time and match again patterns
  f = open(filename, 'r')
  for line in f:
    ymatch = yearp.findall(line)
    if ymatch:
      year = ymatch[0]
      
    nrmatch = name_rankp.findall(line)
    if nrmatch:
      names = sorted([nrmatch[0][1], nrmatch[0][2]])
      rdict[nrmatch[0][0]] = names
  
  # convert dict to list of names and rankings
  for key in rdict.keys():
    result.append(rdict[key][0] + ' ' + key)
    result.append(rdict[key][1] + ' ' + key)
      
  f.close()

  result.sort()
  result.insert(0, year)
  return result

def write_result(result, filename):
  f = open(filename, 'w')
  resultstr = '\n'.join(result) + '\n'
  f.write(resultstr)
  f.flush()
  f.close()

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  fileptrn = re.compile(r'[a-zA-z]+[0-9]+.html')
  outputpath = 'c:/temp/python'
  inputpath = '.' # assume current dir
  filenames = [f for f in listdir(inputpath) if isfile(join(inputpath, f)) and fileptrn.match(f)]
  print(filenames)
  for filename in filenames:
    result = extract_names(filename)
    if summary: write_result(result, join(outputpath, filename + '.summary'))
    else: print('\n'.join(result) + '\n')
if __name__ == '__main__':
  main()
