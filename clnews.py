#!/usr/bin/python
import sys
import cnn_homepage
import hackernews_reader

def quit():
    print '\nThanks for reading!'
    sys.exit(1)

def pick_cnn_article():
    print '\nTo read an article type the headline number.'
    print 'To go back to the main menu, type "main"'
    print 'To quit type quit.\n'
    index = raw_input()
    if index == 'quit':
        quit()
    elif index == 'main':
        main()
    else:
        cnn_homepage.cl_news_util(['cnn', '-r', index])
        read_more('cnn')

def pick_hn_article():
    print '\nTo open an article type the headline number.'
    print 'To go back to the main menu, type "main"'
    print 'To quit type quit.\n'
    index = raw_input()
    if index == 'quit':
        quit()
    elif index == 'main':
        main()
    else:
        hackernews_reader.cl_news_util(['hn', '-o', index])
        read_more('hn')

def read_more(service):
    print '\nWould you like to read more from ' + service + '?(y/n)'
    print 'Type "main" to return to the Main Menu.\n'
    user_input = raw_input()
    if user_input == 'y':
        if service == 'cnn':
            print ''
            cnn_homepage.cl_news_util([service, '-h'])
            read_more(service)
        elif service == 'hn':
            print ''
            hackernews_reader.cl_news_util([service, '-h'])
            read_more(service)
    elif user_input == 'main':
        main()
    elif user_input == 'n':
        quit()
    else:
        print '\nCommand not recognized.\n'
        read_more(service)

def main():
    print '\n======= Command Line News =======\n'
    print 'What would you like to read?\n'
    print 'HackerNews => type: hn'
    print 'CNN => type cnn'
    print 'quit => type: quit'

    service = raw_input()
    if service == 'cnn':
        print '\n'
        cnn_homepage.cl_news_util([service, '-h'])
        pick_cnn_article()
    elif service == 'hn':
        print '\n'
        hackernews_reader.cl_news_util([service, '-h'])
        pick_hn_article()
    elif service == 'quit':
        quit()
    else:
        print '\nCommand not recognized.\n'
        main()

if __name__ == '__main__':
    main()
