# Command Line News
![Alt text](./assets/logo.png 'CLNews logo')


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

### Currently with support for:
- CNN (http://www.cnn.com)
![Alt text](./assets/cnn.png 'CNN logo')
- The Guardian (http://www.theguardian.com/us)
![Alt text](./assets/The_Guardian.png 'The Guardian Logo')
- Associated Press (http://bigstory.ap.org)
![Alt text](./assets/ap.png 'CNN logo')
- Hacker News (http://news.ycombinator.com)
![Alt text](./assets/hacker-news.jpg 'CNN logo')

### Needed:
- Improved Error Handling

### News Services to add:
- reuters
- the new york times
- the washington post

### Features to add:
- remote update, git clone/fetch/rebase updates
- Browser config
