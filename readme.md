# Contents
<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [Major Changes since version 1](#major-changes-since-version-1)
- [What's included](#whats-included)
- [Requirements](#requirements)
- [Instructions](#instructions)
    - [Installation](#installation)
    - [Deployment \(Dreamhost\)](#deployment-dreamhost)
- [Other Resources](#other-resources)
- [Support My Work](#support-my-work)

<!-- /MarkdownTOC -->

*Now updated to Flask 2.0.1*

<a id="major-changes-since-version-1"></a>
## Major Changes since version 1

Flask Assets (along with cssmin and jsmin) are no longer used. These bundlers are quite out of date and have managed to break scripts. I've chosen to replace them with a webpack toolchain for bundling/minification. You may use it, abuse it or lose it. It's up to you.

If you prefer the old configuration, it still works! The dependencies are even up-to-date. You can find the old config on the [v1 branch](https://github.com/trev-dev/flask-starter/tree/v1)

<a id="whats-included"></a>
## What's included

**Bootstrap Version**

In this repo is flask web-app skeleton for a basic API or Flask powered website. Bootstrap 5 is included in the static/vendor folder and you may make whatever changes to static/js or static/css that you'd like. This repository comes pre-setup with Webpack to precompile SASSy styles and Typescript.

[See this project live here](<http://flask-skeleton.trevdev.ca/>)

<a id="requirements"></a>
## Requirements

-   [Python](https://www.python.org/downloads/) (preferably Python3)
-   [Python Pip](https://pip.pypa.io/en/stable/installing/)
-   [Pipenv](https://pipenv.readthedocs.io/en/latest/) for virtualenv & dependency management.

Optionally:
- NodeJS ^14.0 & NPM if you want to use the webpack config, or make your own config

<a id="instructions"></a>
## Instructions

<a id="installation"></a>
### Installation

1.  Clone this repository `git clone git@github.com:trev-dev/flask-starter.git`
2.  Enter the flask-starter directory `cd flask-starter`
3.  Install dependencies and setup virtualenv with `pipenv install`
4.  Start a pipenv shell session with `pipenv shell`
5.  Export your dev environment variables:
    ```bash
    export FLASK_ENV=development
    export FLASK_APP=flaskr
    ```
6.  type `flask run` to start your dev server.  

If you want to use the existing webpack config or make your own, all the usual steps to run npm need to happen. Once you have Node and NPM installed, run `npm install` to install the dependencies. The scripts `npm start` and `npm run build` handle bundling for development and production respectively.

If you just want to write normal JS/CSS you can use the statics found at `flaskr/static/` folder.

<a id="deployment-dreamhost"></a>
### Deployment (Dreamhost)

1.  Setup hosting for a domain and ensure you have [passenger enabled](https://help.dreamhost.com/hc/en-us/articles/216385637-How-do-I-enable-Passenger-on-my-domain) for Python apps.
2.  Use FTP/SFTP/Git to move your project to its destination on Dreamhost (/home/username/example.com).
3.  Double check your Flask config at `flaskr/config.py`. It probably wouldn't hurt to make sure these are not commented out and set for production, especially the SECRET_KEY.
4.  You may need a custom installation of Python3 on Dreamhost for this to work. Please see [Dreamhost's Documentation](https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3) on how to do this. The Pipfile for this repo calls for python 3.9. You may use 3.6 if you update the pipenv Pipfile.
5. Once you've verified a usable Python3 installation, install `pipenv` on your Dreamhost server using `pip3 install pipenv`.
6. From the website root folder, run `pipenv install` to install the dependencies.
    1. If you've installed a custom version of Python, pipenv can be pointed at it with `pipenv --python '/path/to/python/bin/python' install`.
    2. If pipenv isn't on your PATH, you may use `python3 -m pipenv` instead
7. Wait a few minutes, then visit your website. It should be working. If not, Dreamhost has lots of documentation/support that can help you out. Enjoy!

The `passenger_wsgi.py` is set up well enough that it might just work for you without further configuration.

<a id="other-resources"></a>
## Other Resources

If you get stuck it wouldn't hurt to check out:

1. [Flask's Documentation](https://flask.palletsprojects.com/en/2.0.x/)
2. [Dreamhost's Documentation on Python](https://help.dreamhost.com/hc/en-us/articles/216137717)
3. [Brett's Beta](http://www.brettsbeta.com/blog/2020/07/flask-on-dreamhost-shared-website-hosting/) - An amazing guide that I wish had been written before I tried to do this myself.

<a id="support-my-work"></a>
## Support My Work

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y34UWHH) [![Support me on Liberpay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/trev.dev/donate)