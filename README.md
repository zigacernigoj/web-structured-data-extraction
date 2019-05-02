# Web structured data extraction

## About

This is web structured data extraction.

More about it you can read in report.pdf

## Requirements

### Python

Download Python 3.6 or 3.7 from [Python website](https://www.python.org/downloads/). 
We don't guarantee that all libraries work with lower 3.x sub-versions. 
Do not use Python 2.7.

#### Note
All instructions are tested on Linux, we don't guarantee that everything will work on Windows or MacOS.
All further instructions are written with assumption that Python 3 is your default Python 
(be sure to check the PATH or write `python3` and `pip3` instead of `python` and `pip` ).

In case of `EnvironmentError`, run `pip install <module> --user`.
Or you can use pipenv. 
You need to install it first (`pip install pipenv`) and then run `pipenv shell`. 
Note that you must then install needed libraries with `pipenv` not `pip`.

#### Libraries

- Requests: run `pip install requests`
- Lxml: run `pip install lxml`
- BeautifulSoup4: run `pip install bs4`


## Running

Go to implementation folder and run `python extraction.py <params>`

Parameters (`<params>`):
- first parameter: approach (regex: `re` , xpath: `xpath`, road runner: `road`)
- second parameter: page type (rtvslo.si: `rtvslo.si`, overstock.com: `overstock.com`, our choice: `bolha.com`)

## About
This project contains three different approaches for the structured data extraction from the web:

- Using regular expressions
- Using XPath
- RoadRunner-like implementation

The whole report will be available in file `report.pdf`


    
 
