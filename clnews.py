#!/usr/bin/python
import sys
import os

# Append services path to enable imports
sys.path.append('<PATH TO REPOSITORY>')
import cnn
import hackernews
import ap
import guardian
import aljaz
import nyt
import utils

# Handle user selected CNN article by headline number
def pick_article(service):
    utils.command_prompt()
    command = raw_input()

    if command == 'quit':
        utils.quit()
    elif command == 'main':
        main()

    try:
        int(command)
    except:
        pick_article(service)

    if service == 'cnn':
        cnn.cl_news_util(['cnn', '-r', command], cache['cnn'])
    elif service == 'hn':
        # Hacker News is the only read action that opens the page
        hackernews.cl_news_util(['hn', '-o', command], cache['hn'])
    elif service == 'ap':
        ap.cl_news_util(['ap', '-r', command], cache['ap'])
    elif service == 'gu':
        guardian.cl_news_util(['gu', '-r', command], cache['gu'])
    elif service == 'aljaz':
        aljaz.cl_news_util(['aljaz', '-r', command], cache['aljaz'])
    elif service == 'nyt':
        nyt.cl_news_util(['nyt', '-r', command], cache['nyt'])

    read_more(service)

# Control Flow
def read_more(service):
    utils.read_more(service)
    command = raw_input()

    if command == 'main':
        main()
    elif command == 'quit':
        utils.quit()

    if command == 'y':
        print '\n'
        # read more from cnn
        if service == 'cnn':
            cnn.cl_news_util(['cnn', '-h'], cache['cnn'])
        # read more from hackernews
        elif service == 'hn':
            hackernews.cl_news_util(['hn', '-h'], cache['hn'])
        # read more from ap
        elif service == 'ap':
            ap.cl_news_util(['ap', '-h'], cache['ap'])
        # read more from the guradian
        elif service == 'gu':
            guardian.cl_news_util(['gu', '-h'], cache['gu'])
        # read more from al jazeera
        elif service == 'aljaz':
                aljaz.cl_news_util(['aljaz', '-h'], cache['aljaz'])
        # read more from nyt
        elif service == 'nyt':
                nyt.cl_news_util(['nyt', '-h'], cache['nyt'])

        pick_article(service)

    else:
        print '\nCommand not recognized.\n'
        read_more(service)

cache = {
  'cnn': False,
  'hn': False,
  'ap': False,
  'gu': False,
  'aljaz': False,
  'nyt': False
}

def main():
    utils.cl_news_headline()
    service = raw_input()
    print '\n'

    if service == 'cnn':
        cache['cnn'] = cnn.cl_news_util([service, '-h'], cache['cnn'])
    elif service == 'hn':
        cache['hn'] = hackernews.cl_news_util([service, '-h'], cache['hn'])
    elif service == 'ap':
        cache['ap'] = ap.cl_news_util([service, '-h'], cache['ap'])
    elif service == 'gu':
        cache['gu'] = guardian.cl_news_util([service, '-h'], cache['gu'])
    elif service == 'aljaz':
        cache['aljaz'] = aljaz.cl_news_util([service, '-h'], cache['aljaz'])
    elif service == 'nyt':
        cache['nyt'] = nyt.cl_news_util([service, '-h'], cache['nyt'])
    elif service == 'quit':
        utils.quit()
    else:
        print '\nCommand not recognized.\n'
        main()

    pick_article(service)

if __name__ == '__main__':
    main()
