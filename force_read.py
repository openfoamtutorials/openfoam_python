#!/usr/bin/python

import os
import sys
import math
import numpy

def line2dict(line):
  tokens_unprocessed = line.split()
  tokens = [x.replace(")","").replace("(","") \
    for x in tokens_unprocessed]
  floats = [float(x) for x in tokens]
  data_dict = {}
  data_dict['time'] = floats[0]
  force_dict = {}
  force_dict['pressure'] = floats[1:4]
  force_dict['viscous'] = floats[4:7]
  force_dict['porous'] = floats[7:10]
  moment_dict = {}
  moment_dict['pressure'] = floats[10:13]
  moment_dict['viscous'] = floats[13:16]
  moment_dict['porous'] = floats[16:19]
  data_dict['force'] = force_dict
  data_dict['moment'] = moment_dict
  return data_dict

def get_forces_dict(forces_file):
  # Returns a list of lists: [time, drag, lift, moment]
  time = []
  drag = []
  lift = []
  moment = []
  with open(forces_file,"r") as datafile:
    for line in datafile:
      if line[0] == "#":
        continue
      data_dict = line2dict(line)
      time += [data_dict['time']]
      drag += [data_dict['force']['pressure'][0] + \
        data_dict['force']['viscous'][0]]
      lift += [data_dict['force']['pressure'][1] + \
        data_dict['force']['viscous'][1]]
      moment += [data_dict['moment']['pressure'][2] + \
        data_dict['moment']['viscous'][2]]
  datafile.close()
  return [time, drag, lift, moment]

def get_line_from_file(file_path, line_number):
  with open(file_path, "r") as temp_file:
    lines = temp_file.readlines()
  temp_file.close()
  return lines[line_number]
  
def get_overall_chord():
  # Searches file for the chord.
  return float(get_line_from_file("geometry.dat", 0))

def get_cell_depth():
  # Searches file for the cell_depth.
  return float(get_line_from_file("geometry.dat", 1))

def get_V():
  # Searches file for the velocity.
  # We assume we are in the case directory.
  velocity = 0
  with open("0/include/initialConditions","r") as ufile:
    for line in ufile:
      if "flowVelocity" in line:
        vector = line[line.find("(")+1:line.find(")")]
        velocity = float(vector.split()[0])
  ufile.close()
  return velocity

def trailing_average(time, data, trailing_time):
  end_time = time[-1]
  start_time = end_time - trailing_time
  diff = numpy.abs( [x-start_time for x in time] )
  start_index = diff.argmin()
  subdata = data[start_index:len(data)]
  return sum(subdata) / len(subdata)

def get_latest_force_time(patch):
  # Assumes in main case directory
  # Assumes all folders are floating-point named
  # Gets folder with highest floating-point value
  folders = [ float(x) for x in os.listdir("postProcessing/"+patch) ]
  folders.sort()
  folder = folders[-1]
  if folder.is_integer():
    folder = int(folder)
  return folder