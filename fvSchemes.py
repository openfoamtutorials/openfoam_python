#!/usr/bin/python

import os
import file_operations

def second_order_spatial(fvSchemes_path="system/fvSchemes"):
  """
  Assumed format: each setting is on its own line.
  """
  file_operations.change_line(fvSchemes_path, ['div', 'phi', 'U'], ['//'], \
    "\tdiv(phi,U)\t\tGauss linearUpwind grad(U);\n")
  file_operations.change_line(fvSchemes_path, ['div', 'phi', 'k'], ['//'], \
    "\tdiv(phi,k)\t\tGauss limitedLinear 1;\n")
  file_operations.change_line(fvSchemes_path, ['div', 'phi', 'omega'], \
    ['//'], "\tdiv(phi,omega)\tGauss limitedLinear 1;\n")
  file_operations.change_line(fvSchemes_path, ['div', 'phi', 'nut'], \
    ['//'], "\tdiv(phi,nut)\tGauss limitedLinear 1;\n")
  return

def first_order_spatial(fvSchemes_path="system/fvSchemes"):
  """
  Assumed format: each setting is on its own line.
  """
  file_operations.change_line(fvSchemes_path, ['div', 'phi', 'U'], ['//'], \
    "\tdiv(phi,U)\t\tGauss upwind;\n")
  file_operations.change_line(fvSchemes_path, ['div', 'phi', 'k'], ['//'], \
    "\tdiv(phi,k)\t\tGauss upwind;\n")
  file_operations.change_line(fvSchemes_path, ['div', 'phi', 'omega'], \
    ['//'], "\tdiv(phi,omega)\tGauss upwind;\n")
  file_operations.change_line(fvSchemes_path, ['div', 'phi', 'nut'], \
    ['//'], "\tdiv(phi,nut)\tGauss upwind;\n")
  return

