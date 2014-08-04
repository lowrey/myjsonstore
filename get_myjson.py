import base64
import requests
from io import StringIO
import urllib.parse as urlparse
from config import ROOT_URL
import json


from verbose import print_v

GET_URL = "/bins/{}"


# get a file encoded in b64
def get_file(pad_name, outfile):
    f = open(outfile, 'w+b')
    to_decode = StringIO.StringIO()
    to_decode.write(get_content(pad_name))
    to_decode.seek(0)
    base64.decode(to_decode, f)
    f.close()


def get_content(bin_id):
    url = urlparse.urljoin(ROOT_URL, GET_URL.format(bin_id))
    r = requests.get(url)
    print_v("Get successful")
    return json.loads(r.text)


# route to appropriate function
def get(dest, opts):
    if opts.file:
        get_file(dest, opts.file)
    else:
        print(get_content(dest))
