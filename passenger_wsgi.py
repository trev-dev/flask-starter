import sys, os # noqa

INTERP = '/home/<username>/<websitefolder>/env/bin/python'
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from launcher import app as application # noqa