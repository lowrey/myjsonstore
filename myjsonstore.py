#!/usr/bin/python

# import uuid
from optparse import OptionParser
import myjson
from verbose import set_v


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-g", "--get", dest="get", default=None, help="get data from myjson.com")
    parser.add_option("-u", "--update", dest="update", default=None, help="put data from myjson.com")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", \
                      default=False, help="set verbose output")
    parser.add_option("-f", "--file", dest="file", default=None, help="file to upload binary data via base64, "
                                                                      "also used for output directory in get")
    parser.add_option("-i", "--input", dest="input", default=False, \
                      help="input gathered from arg instead of std input")
    (options, args) = parser.parse_args()
    set_v(options.verbose)
    if options.get:
        call = myjson.Get()
    elif options.update:
        call = myjson.Put()
    else:
        call = myjson.Post()
    call.route(options)
