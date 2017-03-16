#!/usr/bin/python
import os

def main():
    currentdir = os.path.abspath('.')
    f = open(currentdir + '/test/twitter.html', 'rU')
    print f.read()
    return

if __name__ == '__main__':
    main()
