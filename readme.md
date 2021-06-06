# Contents
<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [Major Changes since version 1](#major-changes-since-version-1)
- [What's included](#whats-included)
- [Requirements](#requirements)
- [Instructions](#instructions)
    - [Installation](#installation)
    - [Deployment \(Dreamhost\)](#deployment-dreamhost)

<!-- /MarkdownTOC -->

*Now updated to Flask 2.0.1*

<a id="major-changes-since-version-1"></a>
## Major Changes since version 1

Flask Assets (along with cssmin and jsmin) are no longer used. These bundlers are quite out of date and have managed to break scripts. I've chosen to replace them with a webpack toolchain for bundling/minification. You may use it, abuse it or lose it. It's up to you.

<a id="whats-included"></a>
## What's included

**Bootstrap Version**

In this repo is flask web-app skeleton for a basic API or Flask powered website. Bootstrap 5 is included in the static/vendor folder and you may make whatever changes to static/js or static/css that you'd like. This repository comes pre-setup with Webpack to precompile sassy styles and Typescript.

[See this project live here](<http://flask-skeleton.trevdev.ca/>)

<a id="requirements"></a>
## Requirements

-   [Python](https://www.python.org/downloads/) (preferrably Python3)
-   [Python Pip](https://pip.pypa.io/en/stable/installing/)
-   [Pipenv](https://pipenv.readthedocs.io/en/latest/) for virtualenv & dependency management.

<a id="instructions"></a>
## Instructions

<a id="installation"></a>
### Installation

1.  Clone this repository `git clone git@github.com:trev-dev/flask-starter.git`
2.  Enter the flask-starter directory `cd flask-starter`
3.  Install dependencies and setup virtualenv with `pipenv install`
4.  Run the installation with `pipenv run python launcher.py` or by entering `pipenv shell` prior to running `python launcher.py`
5.  Edit/change/develop your site using [Flask + Jinja2](<http://flask.pocoo.org/docs/0.12/>) (Or whatever other templating you wish to use)

<a id="deployment-dreamhost"></a>
### Deployment (Dreamhost)

1.  Setup hosting for a domain and ensure you have [passenger enabled](https://help.dreamhost.com/hc/en-us/articles/216385637-How-do-I-enable-Passenger-on-my-domain) for Python apps.
2.  Use FTP/SFTP/Git to move your project to its destination on Dreamhost (/home/username/example.com). **Be sure to avoid moving any caching or your env**.
3.  You may need a custom installation of Python3 on Dreamhost for this to work. Please see [Dreamhost's Documentation](https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3) on how to do this. The Pipfile for this repo calls for python 3.7. You may use 3.6 if you update the pipenv Pipfile and _delete the pipenv lockfile_.
4. Once you've verified a usable Python3 installation, install `pipenv` on your Dreamhost server using `pip3 install pipenv`.
5. From the website root folder, run `pipenv install` to install the dependencies.
6. Wait a few minutes, then visit your website. It should be working. If not, Dreamhost has lots of documentation/support that can help you out. Enjoy!