# Command Line News
![Alt text](./assets/logo.png 'CLNews logo')
![Alt text](https://www.python.org/static/community_logos/python-powered-w.svg 'Python Logo')


## Set up:
- Download a zip file or clone with git:
  - Download zip here:http://commandlinenews.herokuapp.com
  - or run => ` git clone https://github.com/mickberber/pystuff.git `
- Set Alias in your config file:
  - Bash:
    - open: `.bashrc`
    - add `alias cln='<PATH_TO_REPOSITORY>/clnews.py'`
    - run `source .bashrc`
    - http://www.hostingadvice.com/how-to/set-command-aliases-linuxubuntudebian/
  - Oh My Zsh:
    - open: `.zshrc`
    - add `alias cln='<PATH_TO_REPOSITORY>/clnews.py'` to .zshrc
    - run `source .zshrc`
    - https://stackoverflow.com/questions/14286844/zsh-not-recognizing-my-aliases
- Run `cln` from anywhere in your terminal

## Reporting Bugs
[See bugreport.md](./bugreport.md)

## Contributing
- Fixing Bugs
  - [See bugreport.md](./bugreport.md)
- Adding a service
  - [See addaservice.md](./addaservice.md)

### Currently with support for:
- CNN (http://www.cnn.com)
- The New York Times (http://www.nytimes.com)
- The Guardian (http://www.theguardian.com/us)
- Associated Press (http://bigstory.ap.org)
- Al Jazeera (http://www.aljazeera.com)
- Hacker News (http://news.ycombinator.com)

### Needed:
- Improved Error Handling
- cnn html parsing refactor
- condense main app logic
- file restructuring

### News Services to add:
- Reuters
- The Washington Post
- BBC
- Vice
- Command Line News Twitter Account

### Features to add:
- Remote update
- Config file
- Testing
- Adding Services Documentation

![Alt text](./assets/cnn.png 'CNN logo')
![Alt text](./assets/NYTLogo.jpg 'NYT logo')
![Alt text](./assets/The_Guardian.png 'The Guardian Logo')
![Alt text](./assets/ap.png 'AP logo')
![Alt text](./assets/hacker-news.jpg 'HN logo')
![Alt text](./assets/aljaz.jpg 'Al jaz logo')
