#!/usr/bin/env python
'''
Filename:             slowmover.py
Date Created:         2015-09-27
Date Modified:        2015-09-27
Description:

Moves files inside a directory to another one by one by a specifiend delay in seconds

'''
import sys
import os
from time import sleep

def main():

    # Ensure correct command line arguments
    if len(sys.argv) != 4:
        print "USAGE: %s <source> <destination> <seconds>" %sys.argv[0]
        sys.exit()

    # set variables
    origin = os.path.abspath(sys.argv[1]) # Source folder
    destination = os.path.abspath(sys.argv[2]) # Destination folder
    TIME = int(sys.argv[3]) # Time to pause in seconds

    ALL_FILES = os.listdir(origin)

    # Iterate through all the files
    for ITER, FILE in enumerate(ALL_FILES):
        print "moving file %i of %i: %s" %(ITER+1, len(ALL_FILES), FILE)
        os.rename(os.path.join(origin,FILE),os.path.join(destination,FILE))
        # After every 5 files, pause the program for the specified period in seconds
        if (ITER+1) % 5 == 0:
            sleep(TIME)

if __name__ == '__main__':
    main()
