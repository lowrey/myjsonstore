from base64 import encode
import requests
from verbose import print_v #, write_v
from io import StringIO
import urllib.parse as urlparse
from config import ROOT_URL
import json
import re

POST_URL = "/bins"

def b64encode_tos(infile):
    f = open(infile, 'rb')
    outfile = StringIO.StringIO()
    encode(f, outfile)
    f.close()
    return outfile.getvalue()

def post_file(pad_name, infile):
    instr = b64encode_tos(infile)
    post_content(pad_name, instr)

def post_content(obj):
    url = urlparse.urljoin(ROOT_URL, POST_URL)
    payload = json.dumps(obj)
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=payload, headers=headers)
    r.raise_for_status()
    resp = r.json()
    print_v("Request successful: {}".format(resp["uri"]))
    m = re.search("https://api.myjson.com/bins/(.+)", resp["uri"])
    return m.groups()[0]

def post(dest, opts):
    if opts.file:
        post_file(dest, opts.file)
        return
    data = ""
    if not opts.input:
        data = sys.stdin.read()
    else:
        data = opts.input
    post_content(dest, data)
