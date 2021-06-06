import sys, os, subprocess

os.environ['FLASK_APP'] = 'flaskr'
os.environ['FLASK_ENV'] = 'production'

CMD = ['python3', '-m', 'pipenv', 'run', 'which', 'python3']

INTERP = subprocess.check_output(CMD).strip().decode('utf-8')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from flaskr import application