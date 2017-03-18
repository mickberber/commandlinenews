#!/usr/bin/python
import sys
import os
import commands
import re
import utils

def get_files(dir):
    filenames = os.listdir(dir)
    paths = []
    for filename in filenames:
        match = re.search(r'.py', filename)
        if match:
            path = os.path.join(dir, filename)
            abspath = os.path.abspath(path)
            paths.append(abspath)
    return paths

def to_directory(files, destination):
    destpath = os.path.abspath(destination)
    mkdir_cmd = 'mkdir ' + destpath
    (status, output) = commands.getstatusoutput(mkdir_cmd)
    if status:
        sys.stderr.write('there was an error: ' + output)
        sys.exit(1)

    for f in files:
        cp_cmd = 'cp ' + f + ' ' + destpath
        (st, op) = commands.getstatusoutput(cp_cmd)
        if st:
            sys.stderr.write('there was an error: ' + op)
            sys.exit(1)
    return

def main():
    files = get_files('.')
    to_directory(files, './services')

if __name__ == '__main__':
    main()
