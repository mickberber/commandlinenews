#!/usr/bin/python
import urllib
import os
import json

from keys import wu_key

def cl_news_util(cache):
    response = None
    if not cache:
        #load config
        configfile = os.path.abspath('.') + '/config.json'
        config = open(configfile, 'rU')
        config = json.load(config)

        #create api url & call api
        location = config['state'] + '/' + config['city']
        key = wu_key
        url = 'http://api.wunderground.com/api/' + key + '/conditions/q/' + location + '.json'
        response = urllib.urlopen(url)
        response = json.load(response)
    else:
        response = cache
        
    print response['current_observation']['display_location']['full']
    print response['current_observation']['observation_time']
    print response['current_observation']['weather']
    print response['current_observation']['temperature_string']
    print 'Feels Like:' + response['current_observation']['feelslike_string']
    return response

def main():
    #load config
    configfile = os.path.abspath('.') + '/config.json'
    config = open(configfile, 'rU')
    config = json.load(config)

    #create api url
    location = config['state'] + '/' + config['city']
    key = wu_key
    url = 'http://api.wunderground.com/api/' + key + '/conditions/q/' + location + '.json'
    response = urllib.urlopen(url)
    response = json.load(response)
    print response['current_observation']['display_location']['full']
    print response['current_observation']['observation_time']
    print response['current_observation']['weather']
    print response['current_observation']['temperature_string']
    print 'Feels Like:' + response['current_observation']['feelslike_string']
    return

if __name__ == '__main__':
    main()
