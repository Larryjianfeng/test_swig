from .main import args, cut, cat
import sys


def ex():
    arguments = args()
    rs = getattr(sys.modules[__name__], arguments.mode)(arguments.line)
    print('the result is: ', rs)

all = ['ex']