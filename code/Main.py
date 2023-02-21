"""
gird.lua : a rep grid processor

USAGE: grid.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump    on crash, dump stack   = False
  -f  --file    name of file           = ../etc/data/repgrid1.csv
  -g  --go      start-up action        = data
  -h  --help    show help              = False
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211
"""
import getopt
import re
import sys

import TestEngine


def coerce(s):
    "coerce a string to some type"
    s = s.strip()
    if s == "False":
        return False
    elif s == "True":
        return True
    try:
        return int(s)
    except:
        try:
            return float(s)
        except:
            return s


def get_default():
    global the
    p = r"\n[\s]+-[\S]+[\s]+--([\S]+)[^\n]+= ([\S]+)"
    for k, v in re.findall(p, __doc__):
        the[k] = coerce(v)
    # return t


def update(opts, t):
    for opt, arg in opts:
        if opt in ("-d", "--dump"):
            t['dump'] = coerce(arg)
        if opt in ("-f", "--file"):
            t['file'] = coerce(arg)
        if opt in ("-g", "--go"):
            t['go'] = coerce(arg)
        if opt in ("-h", "--help"):
            t['help'] = coerce(arg)
        if opt in ("-p", "--p"):
            t['p'] = coerce(arg)
        if opt in ("-s", "--seed"):
            t['seed'] = coerce(arg)
    return t


# Stores arguments in the variable
# use python3 Main.py --[options]
the = {}
if __name__ == "__main__":
    get_default()
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, ":dfghps", ["dump=", "file=", "go=", "help=", "p=", "seed="])
    except getopt.GetoptError:
        print('Please provide appropriate arguments')
        sys.exit(2)
    the = update(opts, the)
    if the['help']:
        print(__doc__)
        sys.exit(2)
    sys.exit(TestEngine.run(the))
