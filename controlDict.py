#!/usr/bin/python

import os
import file_operations

def set_end_time(new_end_time, case_path="./"):
  controlDict_path = case_path+"/system/controlDict"
  output_file = open(controlDict_path+"_temp", 'w')
  with open(controlDict_path, 'r') as input_file:
    for line in input_file:
      if ("endTime" in line) and ("stopAt" not in line):
        time_value = line.split()[1]
        new_line = line.replace(time_value, str(new_end_time)+";")
        output_file.write(new_line)
      else:
        output_file.write(line)
  output_file.close()
  os.system("mv "+controlDict_path+"_temp "+controlDict_path)
  return

def set_write_interval(new_write_interval, case_path="./"):
  controlDict_path = case_path+"/system/controlDict"
  output_file = open(controlDict_path+"_temp", 'w')
  with open(controlDict_path, 'r') as input_file:
    for line in input_file:
      if ("writeInterval" in line):
        time_value = line.split()[1]
        new_line = line.replace(time_value, str(new_write_interval)+";")
        output_file.write(new_line)
      else:
        output_file.write(line)
  output_file.close()
  os.system("mv "+controlDict_path+"_temp "+controlDict_path)
  return

def set_courant_number(controlDict_path="system/controlDict", maxCo=1):
  file_operations.change_line(controlDict_path, ["maxCo"], \
    [], "\tmaxCo\t\t"+str(maxCo)+";\n")
  return

def set_force_output_interval(controlDict_path="system/controlDict", \
  outputInterval=50):
  file_operations.change_line(controlDict_path, ["outputInterval"], \
    [], "\t\toutputInterval\t\t"+str(outputInterval)+";\n")
  return
