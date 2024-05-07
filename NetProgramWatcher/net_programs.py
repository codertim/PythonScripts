
# this program watches sensitive directories to check if new files were added

import os
import platform
import time
import sys

print("Starting ...")
os_name = platform.system()
print("OS name: ", os_name)

print("cl args:", sys.argv)

is_debugging = False

if "debug" in sys.argv:
    is_debugging = True

programs = {}
while 1 == 1:
  results = ""

  if os_name == "Linux":
      results = os.popen("lsof -i").read()
  elif os_name == "Windows":
      results = os.popen("dir /B").read()

  # print("Results:", results)

  i = 0
  for r in results.splitlines():
      # print("  current line: ", r)
      # if i != 0:
          # print(r)
      cols = r.split()
      if is_debugging == True:
          print("cols", cols)
      # print("cols[0]", cols[0])
      if cols[0] not in programs:
          programs[cols[0]] = 1
          print("********** New program:", cols[0], "**********")
      i+=1

  # print results
  # print results.splitlines()
  # print(programs)
  # print("Keys ...")
  # for k in programs.keys():
  #     print(k)

  if is_debugging:
      print("sleeping ...")
  time.sleep(3)

print("Done.")

