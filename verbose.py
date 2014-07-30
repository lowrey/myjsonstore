import sys

verbose = False
NOTEPAD_CC_URL = 'http://notepad.cc/'

def set_v(v):
    global verbose
    verbose = v

def print_v(s):
    if verbose:
        print(s)

def write_v(s):
    if verbose:
        sys.stdout.write()
