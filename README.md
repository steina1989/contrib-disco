# Contribution Disco !
A UI and script generator to draw graphics on your Github contribution page.

It utilizes a feature of git commit, in which a --date flag can be passed along with the commit. 

## Prerequisites
* Github account
* Web browser
* Python3
* Git

## Usage
```
$ python3 main.py --help
usage: main.py [-h] remote

Draws on the contribution graph of a given Github user's repo.

positional arguments:
  remote      A github repository. Ex:
              https://github.com/yourUser/emptyRepository.git

optional arguments:
  -h, --help  show this help message and exit
```

A script 'out.sh' or 'out.bat' is generated inside the root folder. You should move it to a new empty folder and run it from there.
```
mkdir testrun
mv out.sh testrun
cd testrun
./out.sh
```

If you are thinking about executing the script without at least reading through if it first, think again.

## This has been a part of the 2019 Monthly Programming Challenge for February.
Don't try to to Google it, I just made it up. 
The outcome isn't perfect, but I had fun with it.

Please consider the benefits of programming regularly.