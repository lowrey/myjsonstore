#!/usr/bin/python

#import uuid
from optparse import OptionParser
from get_myjson import get
from post_myjson import post
from verbose import set_v


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--dest", dest="dest", help="destination for output")
    parser.add_option("-g", "--get", dest="get", default=None, help="get data from myjson.com")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true",\
        default=False, help="set verbose output")
    parser.add_option("-f", "--file", dest="file", default=None, help="file to upload binary data via uuencode")
    parser.add_option("-i", "--input", dest="input", default=False, \
        help="input gathered from arg instead of std input")
    (options, args) = parser.parse_args()
    dest = options.dest
    set_v(options.verbose)
    if options.get:
        get(dest, options)
    else:
        #print("Using pad name {}".format(options.dest))
        post(dest, options)
