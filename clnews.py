#!/usr/bin/python
import sys
import cnn
import hackernews

#Handle user quitting
def quit():
    print '\nThanks for reading!'
    sys.exit(1)

#Print Utils
def cl_news_headline():
    print '\n======= Command Line News =======\n'
    print 'What would you like to read?\n'
    print 'HackerNews => type: hn'
    print 'CNN => type cnn\n'
    print 'quit => type: quit'

def command_prompt():
    print '\nTo read an article type the headline number.'
    print 'To go back to the main menu, type "main"'
    print 'To quit type quit.\n'

#Handle user selected CNN article by headline number
def pick_cnn_article():
    command_prompt()
    command = raw_input()
    if command == 'quit':
        quit()
    elif command == 'main':
        main()
    else:
        cnn.cl_news_util(['cnn', '-r', command], cache['cnn'])
        read_more('cnn')

#Handle user selected HackerNews article by headline number
def pick_hn_article():
    command_prompt()
    command = raw_input()
    if command == 'quit':
        quit()
    elif command == 'main':
        main()
    else:
        hackernews.cl_news_util(['hn', '-o', command], cache['hn'])
        read_more('hn')

cache = {
  'cnn': False,
  'hn': False
}

#CNN HN Control Flow
def read_more(service):
    print '\nWould you like to read more from ' + service + '?(y/n)'
    print 'Type "main" to return to the Main Menu.\n'
    user_input = raw_input()
    if user_input == 'y':
        #read more from cnn
        if service == 'cnn':
            print '\n'
            cnn.cl_news_util([service, '-h'], cache['cnn'])
            read_more(service)
        #read more from hackernews
        elif service == 'hn':
            print '\n'
            hackernews.cl_news_util([service, '-h'], cache['hn'])
            read_more(service)
    #go back to main menu
    elif user_input == 'main':
        main()
    #handle quit
    elif user_input == 'n':
        quit()
    else:
        print '\nCommand not recognized.\n'
        read_more(service)

def main():
    cl_news_headline()
    service = raw_input()
    if service == 'cnn':
        print '\n'
        cache['cnn'] = cnn.cl_news_util([service, '-h'], cache['cnn'])
        pick_cnn_article()
    elif service == 'hn':
        print '\n'
        cache['hn'] = hackernews.cl_news_util([service, '-h'], cache['hn'])
        pick_hn_article()
    elif service == 'quit':
        quit()
    else:
        print '\nCommand not recognized.\n'
        main()

if __name__ == '__main__':
    main()
