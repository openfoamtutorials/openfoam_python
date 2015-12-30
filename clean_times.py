#!/usr/bin/python

import os
import sys

def leave_last_time(time_path):
  """
  This leaves the latest time in either processor or main case folders.
  """
  files = os.listdir(time_path)

  num_files = [ \
    float(x) for x in files if ('.' in x or x.isdigit()) \
      and os.path.isdir(x) \
      and (x!="0") ]
  num_files = [ int(x) if x.is_integer() else x for x in num_files ]

  max_time = 0
  if len(num_files) > 1:
    max_time = max(num_files)
    num_files.remove(max_time)
    num_file_names = ' '.join(str(x) for x in num_files)
    os.system("rm -r "+num_file_names)

  return 

print leave_last_time("./")
