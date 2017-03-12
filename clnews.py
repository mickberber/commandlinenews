#!/usr/bin/python
import sys
import cnn_homepage
import hackernews_reader

def quit():
    print 'Thanks for reading!'
    sys.exit(1)

def read_more():
    print ''
    print 'Would you like to read more?(y/n)'
    user_input = raw_input()
    if user_input == 'y':
        main()
    elif user_input == 'n':
        quit()
    else:
        read_more()

def main():
    print ''
    print '======= Command Line News ======='
    print ''
    print 'What would you like to read?'
    print 'HackerNews => Usage: hn [--headlines -h] [--open -o][headline number] [--copy -cp][dest filename]'
    print 'CNN => Usage: cnn [--headlines -h] [--read -r][headline number] [--open -o][headline number]'
    print 'quit => quit'

    user_input = raw_input()
    user_input = user_input.split(' ')
    if user_input[0] == 'cnn':
        print ''
        cnn_homepage.cl_news_util(user_input)
        read_more()
    elif user_input[0] == 'hn':
        print ''
        hackernews_reader.cl_news_util(user_input)
        read_more()
    elif user_input[0] == 'quit':
        quit()
    else:
        print ''
        print 'Command not recognized.'
        print ''
        main()

if __name__ == '__main__':
    main()
