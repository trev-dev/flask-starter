import sys, os, subprocess

CMD = ['pipenv', 'run', 'which', 'python3']

INTERP = subprocess.check_output(CMD).strip().decode('utf-8')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from flaskr import application