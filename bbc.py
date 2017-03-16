#!/usr/bin/python
import os
import utils
import json

def main():
    currentdir = os.path.abspath('.')
    f = open(currentdir + '/test/bbc.html', 'rU')
    print f.read()
    return

if __name__ == '__main__':
    main()
