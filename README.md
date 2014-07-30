myjsonstore
========

Myjsonstore is a command line interface to myjson.com service. Input can be taken but stdin, argument, or a file.  If a file is given, it is stored on myjson.com as base64 encoded data.  Output is by default written to stdout but can be written to a file.  Content is base64 decoded if written to a file.

## Examples
* ./myjsonstore.py -i "not your json"
* ./myjsonstore.py -g 55 -d OutputFile
* ./myjsonstore.py -d FileExample -f rykr.jpeg
