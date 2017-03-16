#!/usr/bin/python
import sys
import os

import utils

from HTMLParser import HTMLParser

def read_config():
    with open('config.json') as json_file:
        json_data = json.load(json_file)
        print json_data['this']
    return

def cnn_tests():
    return

def hn_tests():
    return

def main():
    return

if __name__ == '__main__':
    main()
