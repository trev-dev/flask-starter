
# Table of Contents

1.  [Flask Starter Web Application](#intro)
    1.  [What's included](#included)
    2.  [Requirements](#requirements)
    3.  [Instructions](#instructions)
        1.  [Installation](#installation)
        2.  [Deployment (Dreamhost)](#deployment)


<a id="intro"></a>

# Flask Starter Web Application

*Now updated to Flask 1.0.2*


<a id="included"></a>

## What's included

In this repo is flask web-app skeleton for a basic API or Flask powered website. The stylesheets are Sassy and Bootstrap 4 is included in the Sass libs folder. Everything you need here (except a Sass precompiler) to get started with a Flask App along with deployment instructions for Dreamhost.

[See this project live here](<http://flask-skeleton.trevdev.ca/>)


<a id="requirements"></a>

## Requirements

-   [Python](https://www.python.org/downloads/) (preferrably Python3)
-   [Python Pip](https://pip.pypa.io/en/stable/installing/)
-   [Pipenv](https://pipenv.readthedocs.io/en/latest/) for virtualenv & dependency management.
-   SASS/SCSS compiler (or not, it's up to you. My SASS files are included in the repo.)


<a id="instructions"></a>

## Instructions


<a id="installation"></a>

### Installation

1.  Clone this repository `git clone git@github.com:trev-dev/flask-starter.git`
2.  Enter the flask-starter directory `cd flask-starter`
3.  Install dependencies and setup virtualenv with `pipenv install`
4.  Run the installation with `pipenv run python launcher.py` or by entering `pipenv shell` prior to running `python launcher.py`
5.  Edit/change/develop your site using [Flask + Jinja2](<http://flask.pocoo.org/docs/0.12/>) (Or whatever other templating you wish to use)

<a id="deployment"></a>

### Deployment (Dreamhost)

1.  Setup hosting for a domain and ensure you have [passenger enabled](https://help.dreamhost.com/hc/en-us/articles/216385637-How-do-I-enable-Passenger-on-my-domain) for Python apps.
2.  Use FTP/SFTP/Git to move your project to its destination on Dreamhost (/home/username/example.com). **Be sure to avoid moving any caching or your env**.
3.  You may need a custom installation of Python3 on Dreamhost for this to work. Please see [Dreamhost's Documentation](https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3) on how to do this. The Pipfile for this repo calls for python 3.7. You may use 3.6 if you update the pipenv Pipfile and _delete the pipenv lockfile_.
4. Once you've verified a usable Python3 installation, install `pipenv` on your Dreamhost server using `pip3 install pipenv`.
5. From the website root folder, run `pipenv install` to install the dependencies.
6. Wait a few minutes, then visit your website. It should be working. If not, Dreamhost has lots of documentation/support that can help you out. Enjoy!