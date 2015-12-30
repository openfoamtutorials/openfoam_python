#!/usr/bin/python

import os
import file_operations

def set_piso_correctors(nCorrectors, fvSolution_path="system/fvSolution"):
  """
  Assumed format: each setting is on its own line.
  """
  file_operations.change_line(fvSolution_path, ['nCorrectors', ';'], ['//'], \
    "\tnCorrectors\t\t"+str(nCorrectors)+";\n")
  return
