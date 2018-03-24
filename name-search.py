#!/usr/local/bin/python3

import re

num_inputs = int(input())
inputs = []

for i in range(0, num_inputs):
  srl = i+1
  inputs.append(input())

for string in inputs:
  suvos = re.findall('SUVO', string)
  suvojits = re.findall('SUVOJIT', string)

  # If we find both partial matches and full matches, 
  # remove as many partials as there are full matches,
  # since the partials are contained in the fulls.
  # Also, no need to check for len(suvos) > 0, because
  # re.findall() will have found the partial match in
  # the full match
  if (len(suvojits) > 0):
    for i in range(0, len(suvojits)):
      del(suvos[0])

  print("SUVO =", str(len(suvos)) + ',', "SUVOJIT =", len(suvojits))