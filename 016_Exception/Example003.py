#!/usr/bin/python

try:
   fh = open("testfile", "r")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print("Going to close the file")
      fh.close()
except IOError:
   print("Error: can\'t find file or read data")
finally:
    print("Closing App")
