---
layout: post
title: "Chapter 1: Setting Things Up"
---

In this chapter, we will discuss the required software as well as how to generate an environment for your web scraper. 

## Required Software
1. [Google Chrome](https://www.google.com/chrome/browser/desktop/index.html)
2. [Firefox](https://www.mozilla.org/en-US/firefox/new/)
3. [disable-HTML](https://chrome.google.com/webstore/detail/disable-html/lfhjgihpknekohffabeddfkmoiklonhm)
4. [Sublime Text](https://www.sublimetext.com/)
5. [python 2.7](https://www.python.org/downloads/)
6. [pip](https://pypi.python.org/pypi/pip)
```bash
# Linux
~$ sudo apt-get install python-pip
# Mac OS
~$ brew install python
```
7. [virtualenv](https://pypi.python.org/pypi/virtualenv)
```bash
~$ pip install virtualenv
```

## Creating the Work Environment
### Installing
1\. Open Terminal

2\. Navigate to the directory you want to store your project in

```bash
~$ cd Desktop/
```

3\. Make a new directory for your project

```bash
~/Desktop$ mkdir sample-scrapers
```

4\. Navigate into this directory

```bash
~/Desktop$ cd sample-scrapers/
```

5\. Create a virtual environment for your python packages

```bash
~/Desktop/sample-scrapers/$ virtualenv env
```

6\. Activate the virtual environment

```bash
~/Desktop/sample-scrapers/$ source env/bin/activate
```

7\. Install the needed python packages

```bash
(env) ~/Desktop/sample-scrapers/$ pip install BeautifulSoup
(env) ~/Desktop/sample-scrapers/$ pip install requests
(env) ~/Desktop/sample-scrapers/$ pip install mechanize
(env) ~/Desktop/sample-scrapers/$ pip install selenium
(env) ~/Desktop/sample-scrapers/$ pip install xmltodict
```

### Testing
Let's confirm that the virtual environment is set up properly and ready for development. Type in the following import statements. We want to make sure everything is installed before proceeding to the next chapter.
```bash
(env) ~/Desktop/sample-scrapers/$ python
Python 2.7.12 (default, Nov 30 2016, 12:04:04) 
>>> from BeautifulSoup import BeautifulSoup
>>> import requests
>>> import mechanize
>>> import selenium
>>> import xmltodict
```
