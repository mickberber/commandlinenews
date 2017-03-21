# Command Line News
![Alt text](./assets/cln_output.png 'CLNews logo')

## Set up:
- Download a zip file or clone with git:
  - Download zip here:http://commandlinenews.herokuapp.com
  - or run => ` git clone https://github.com/mickberber/pystuff.git `
- Set Alias in your config file:
  - Bash:
    - `$ .bashrc`
    - `$ alias cln='<PATH_TO_REPOSITORY>/clnews.py'`
    - `$ source .bashrc`
    - http://www.hostingadvice.com/how-to/set-command-aliases-linuxubuntudebian/
  - Oh My Zsh:
    - `$ .zshrc`
    - `$ alias cln='<PATH_TO_REPOSITORY>/clnews.py'` to .zshrc
    - `$ source .zshrc`
    - https://stackoverflow.com/questions/14286844/zsh-not-recognizing-my-aliases
- Create `keys.py` and add path:
  - `$ touch keys.py`
  - Inside of keys.py, add a PATH variable equal to the path to your repository:
    - ex. PATH='PATH_TO_REPOSITORY'
- Run `cln` from anywhere in your terminal

## Reporting Bugs
[See bugreport.md](./DOCS/bugreport.md)

## Contributing
- Fixing Bugs
  - [See bugreport.md](./DOCS/bugreport.md)
- Adding a service
  - [See addaservice.md](./DOCS/addaservice.md)

### Currently with support for:
- CNN (http://www.cnn.com)
- The New York Times (http://www.nytimes.com)
- The Washington Post (http://www.washingtonpost.com)
- The Guardian (http://www.theguardian.com/us)
- Associated Press (http://bigstory.ap.org)
- Al Jazeera (http://www.aljazeera.com)
- Hacker News (http://news.ycombinator.com)

### Needed:
- Improved Error Handling
- cnn html parsing refactor
- condense main app logic

### News Services to add:
- Reuters
- BBC
- Vice

### Features to add:
- Remote update
- Testing
