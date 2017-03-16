#!/usr/bin/python
import sys
import os
import cnn
import hackernews
import ap
import guardian
import utils

#Handle user selected CNN article by headline number
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
        read_more('cnn')
    elif service == 'hn':
        hackernews.cl_news_util(['hn', '-o', command], cache['hn'])
        read_more('hn')
    elif service == 'ap':
        ap.cl_news_util(['ap', '-r', command], cache['ap'])
        read_more('ap')
    elif service == 'gu':
        guardian.cl_news_util(['gu', '-r', command], cache['gu'])
        read_more('gu')


#Control Flow
def read_more(service):
    print '\nWould you like to read more from ' + service + '?(y/n)'
    print 'Type "main" to return to the Main Menu.\n'
    user_input = raw_input()
    if user_input == 'y':
        #read more from cnn
        if service == 'cnn':
            print '\n'
            cnn.cl_news_util(['cnn', '-h'], cache['cnn'])
            pick_article('cnn')
        #read more from hackernews
        elif service == 'hn':
            print '\n'
            hackernews.cl_news_util(['hn', '-h'], cache['hn'])
            pick_article('hn')
        #read more from ap
        elif service == 'ap':
            print '\n'
            ap.cl_news_util(['ap', '-h'], cache['ap'])
            pick_article('ap')
        #read more from the guradian
        elif service == 'gu':
            print '\n'
            guardian.cl_news_util(['gu', '-h'], cache['gu'])
            pick_article('gu')

    #go back to main menu
    elif user_input == 'main':
        main()
    #handle quit
    elif user_input == 'n':
        utils.quit()
    else:
        print '\nCommand not recognized.\n'
        read_more(service)

cache = {
  'cnn': False,
  'hn': False,
  'ap': False,
  'gu': False
}

def main():
    utils.cl_news_headline()
    service = raw_input()
    if service == 'cnn':
        print '\n'
        cache['cnn'] = cnn.cl_news_util([service, '-h'], cache['cnn'])
        pick_article('cnn')
    elif service == 'hn':
        print '\n'
        cache['hn'] = hackernews.cl_news_util([service, '-h'], cache['hn'])
        pick_article('hn')
    elif service == 'ap':
        print '\n'
        cache['ap'] = ap.cl_news_util([service, '-h'], cache['ap'])
        pick_article('ap')
    elif service == 'gu':
        print '\n'
        cache['gu'] = guardian.cl_news_util([service, '-h'], cache['gu'])
        pick_article('gu')
    elif service == 'quit':
        utils.quit()
    else:
        print '\nCommand not recognized.\n'
        main()

if __name__ == '__main__':
    main()
