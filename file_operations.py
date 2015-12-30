#!/usr/bin/python

import os

def safely_remove_file(path):
  if os.path.isfile(path):
    os.system("rm "+path)
  return

def safely_remove_dir(path):
  if os.path.isdir(path):
    os.system("rm -r "+path)
  return

def change_file_name(file_path, suffix):
  # Simply adds a suffix to an existing file.
  if os.path.isfile(file_path):
    os.system("mv "+file_path+" "+file_path+suffix)
  else:
    print "Couldn\'t find "+file_path
  return


def get_highest_folder(path, prefix):
  # Assumes that the folders in path are part of a series with an integer ID 
  # as the suffix.
  # Assumes integer ranks
  highest = -1
  folders = [x for x in os.listdir(path) if os.path.isdir(path+"/"+x)]
  for folder in folders:
    folder_id = int(folder.replace(prefix, ""))
    if folder_id > highest:
      highest = folder_id
  return highest


def get_time_folders(case_path="./"):
  time_folders = [ x for x in os.listdir(case_path) \
    if os.path.isdir(case_path+"/"+x) \
    and (("." in x) or (x.isdigit())) \
    and x != "0"]
  return time_folders

def leave_last_time(case_path="./"):
  # if os.path.isdir(case_path+"/processor0"):
    # os.system("reconstructPar -latestTime -case "+case_path)
    # os.system("rm -r processor*")
  time_folders = get_time_folders(case_path)
  times = [ float(x) for x in time_folders ]
  times = [ int(x) if x.is_integer() else x for x in times ]
  times.sort()
  time_folders = [ str(x) for x in times ]
  # print "Here comes the annoying warning"
  if len(time_folders) > 1:
    time_folders_string = ' '.join(time_folders[0:-1])
    os.system("rm -r "+time_folders_string)
  # print "There goes the annoying warning"
  return

def clean_case(case_path="./"):
  # This removes all non-standard FOLDERS.
  current_folders = os.listdir(case_path)
  standard_folders = ["0", "system", "constant", "openfoam_python"]
  # First make sure this is a case!
  for sf in standard_folders:
    if sf not in current_folders:
      print "This is not an OpenFOAM case directory! Be careful! Exiting."
      return
  # Then filter out folders that are not standard folders and remove.
  folders = [ case_path+"/"+x for x in current_folders \
    if os.path.isdir(case_path+"/"+x) and x not in standard_folders ]
  if len(folders) > 0:
    os.system("rm -r "+' '.join(folders))
  # File removal
  if os.path.isfile(case_path+"/geometry.dat"):
    os.system("rm "+case_path+"/geometry.dat")
  if os.path.isdir(case_path+"/constant/polyMesh"):
    os.system("rm -r "+case_path+"/constant/polyMesh")
  if os.path.isfile(case_path+"/main.msh"):
    os.system("rm "+case_path+"/main.msh")
  if os.path.isfile(case_path+"/forces.txt"):
    os.system("rm "+case_path+"/forces.txt")
  # We assume we have reconstructed already.
  if os.path.isdir(case_path+"/processor0"):
    os.system("rm -r "+case_path+"/processor*")
  return

def change_line(file_path, included_strings, excluded_strings, replacement):
  """
  Goes through file_path line-by-line and if all of included_strings are in 
  the line and all of excluded_strings are not in the line, then the whole line 
  is replaced by replacement.
  Assumes file_path+'_temp' is not already a file.
  """
  if not os.path.isfile(file_path):
    print file_path+" file not found!"
    return
  temp_path = file_path+"_temp"
  temp_file = open(temp_path, 'w')
  with open(file_path, 'r') as f:
    for line in f:
      if all([x in line for x in included_strings]) and \
        all([x not in line for x in excluded_strings]):
        temp_file.write(replacement)
      else:
        temp_file.write(line)
  temp_file.close()
  os.system("mv "+temp_path+" "+file_path)
  return
