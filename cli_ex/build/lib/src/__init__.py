from main import args, cut, cat


def ex():
    arguments = args()
    rs = getattr(arguments.mode)(arguments.line)
    print('the result is: ', rs)

all = ['ex']