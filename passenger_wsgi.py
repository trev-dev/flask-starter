import sys, os # noqa

INTERP = '/home/user/<website.com>/env/bin/python'
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from app import app as application # noqa