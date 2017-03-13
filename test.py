#!/usr/bin/python

import utils

def main():
    htmlfile = utils.get_html_file('http://news.ycombinator.com')
    utils.copy_file('/test/hn.html', htmlfile)
    return

if __name__ == '__main__':
    main()
