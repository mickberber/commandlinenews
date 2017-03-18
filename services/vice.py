#!/usr/bin/python
import urllib2
import utils


def get_html_file(url):
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    uf = urllib2.urlopen(req)
    return uf.read()

def main():
    htmlfile = get_html_file('https://news.vice.com/story/abortion-behind-bars-terminating-a-pregnancy-in-prison-can-be-next-to-impossible')
    utils.copy_file('test/vice_article.html', htmlfile)
    return

if __name__ == '__main__':
    main()
