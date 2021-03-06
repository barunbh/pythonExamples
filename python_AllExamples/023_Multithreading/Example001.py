#!/usr/bin/python

import time
from _thread import *

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   start_new_thread( print_time, ("Thread-1", 1, ) )
   start_new_thread( print_time, ("Thread-2", 0, ) )

except:
   print("Error: unable to start thread")

while 1:
   pass