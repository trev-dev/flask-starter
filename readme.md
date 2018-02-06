# Flask Starter Web Application
## What's included
In this repo is flask web-app skeleton for a basic API or Flask powered website. The stylesheets are Sassy and Bootstrap 4 is included in the Sass libs folder. Everything you need here (except a Sass precompiler) to get started with a Flask App along with deployment instructions for Dreamhost.

[See this project live here](http://flask-skeleton.trevdev.ca/)
## Requirements
- [Python](https://www.python.org/downloads/) (preferrably Python3) 
- [pip package manager](https://pip.pypa.io/en/stable/installing/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/) for managing virtual environments (installed via pip)
- SASS/SCSS compiler (or not, it's up to you. My SASS files are included in the repo.)
## Instructions
#### Installation
1) Clone this repository
```
git clone git@github.com:trev-dev/flask-starter.git
```
2) Enter the flask-starter directory
3) Setup your virtual environment (virtualenv) and activate your env.
```
virtualenv env
source ./env/bin/activate
```
4) When you see the little (env) indicator on your terminal, install the python package dependancies.
```
pip install -r requirements.txt
```
5) Launch the app and preview it in your browser on localhost:5000.
```
python app.py
```

6) Edit/change/develop your site using [Flask + Jinja2](http://flask.pocoo.org/docs/0.12/) (Or whatever other templating you wish to use)

#### Deployment (Dreamhost)
1) Setup hosting for a domain and ensure you have [passenger enabled](https://help.dreamhost.com/hc/en-us/articles/216385637-How-do-I-enable-Passenger-on-my-domain-) for Python apps.
2) Use FTP/SFTP to move your project to its destination on Dreamhost (/home/username/example.com). *Be sure to avoid moving any caching or your env*.
3) Use a secure shell to log in to your dreamhost hosting and run the same steps to setup your pip and virtualenv. If your python is out of date on Dreamhost, you can update it/install your own version.
4) Configure passenger_wsgi.py to tie-in passenger to your application - specifically the destination of the python file inside ./env/bin/python. You'll need to change the "website" and username in the INTERP string.


```python
import sys, os

INTERP = '/home/<username>/<website.com>/env/bin/python'
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from app import app as application
```
5) Wait a few minutes, then visit your website. It should be working. If not, Dreamhost has lots of documentation/support that can help you out. Enjoy!