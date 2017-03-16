#!/usr/bin/python
import os
import utils

def main():
    currentdir = os.path.abspath('.')
    htmlfile = utils.get_html_file('http://www.bbc.com/news')
    utils.copy_file('test/bbc.html', htmlfile)
    f = open(currentdir + '/test/bbc.html', 'rU')
    print f.read()
    return

if __name__ == '__main__':
    main()
