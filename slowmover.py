#!/usr/bin/env python
'''
Filename:             slowmover.py
Date Created:         2015-09-27
Date Modified:        2015-09-27
Author:               Bastiaan van der Laaken
email:                mannerisms@gmail.com
Description:

Moves files inside a directory to another one by one by a specifiend delay in seconds

'''
import sys
import os
from time import sleep

def main():

    if len(sys.argv) != 4:
        print "USAGE: %s <source> <destination> <seconds>" %sys.argv[0]
        sys.exit()

    # set variables
    origin = os.path.abspath(sys.argv[1])
    destination = os.path.abspath(sys.argv[2])
    TIME = int(sys.argv[3])

    ALL_FILES = os.listdir(origin)
    for ITER, FILE in enumerate(ALL_FILES):
        print "moving file %i of %i: %s" %(ITER+1, len(ALL_FILES), FILE)
        os.rename(os.path.join(origin,FILE),os.path.join(destination,FILE))
        if (ITER+1) % 5 == 0:
            sleep(TIME)

if __name__ == '__main__':
    main()
