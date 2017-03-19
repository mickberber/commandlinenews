# Command Line News
![Alt text](./assets/cln_output.png 'CLNews logo')

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

### Features to add:
- Remote update
- Config file
- Testing
- Adding Services Documentation

Link to web app code:
https://github.com/mickberber/commandlinenews_page
