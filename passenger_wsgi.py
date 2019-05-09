import sys, os, subprocess # noqa

CMD = ['pipenv', 'run', 'which', 'python3']

INTERP = subprocess.check_output(CMD).strip().decode('utf-8')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from launcher import app as application # noqa
