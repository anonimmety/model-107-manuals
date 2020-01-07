# Mercedes Model 107 Repair Manual Downloader
Download Mercedes R107/C107 repair manuals from Startek.

# Motivation

The complete manual is comprised of hundreds of PDFs organized
in tidy directories. I didn't find a Chrome extension that
would download them all and preserve the folder structure,
so I wrote this.

# Disclaimers

The author of this program makes no representations about its legality.
There may be copyright concerns. If you have any doubts, 
do not use this program, and/or check with a 
copyright expert. 
It's also good form to ask the site owner for
permission.
Because the files are publicly available for download on
the Startek website, the author is assuming it's OK to
download them using this program.

Very little error handling is in the program because it just
wasn't necessary.

# Assumptions

The files will be downloaded to your `~/Downloads/mercedes` folder. You can change
the `local_root` variable if you want them downloaded somewhere else.

This program downloads the files for the 1988 560SL. No other models or years
have been tested because I only care about the '88 :D

Modifying it for other models should be trivial. Available options are on 
[this page](https://www.startekinfo.com/StarTek/outside/11883/?requestedDocId=11883). 
Hover over the model name and a list of model years will appear. Right-click on the
model year you want and copy the URL, and set the `base` variable to that URL.

# Setup

## Requirements

* python 3.6+
  * [Installation instructions](https://www.python.org/downloads/)
* `pip3` 
  * should be installed with python 3
* `virtualenv` 
  * don't have it? install it with `pip3 install virtualenv`

## How To Use

* create a virtual environment, activate, and install libraries:
```
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

* run the program:
```
python download.py
```

* deactivate the virtual environment when you're done:
```
deactivate
```
