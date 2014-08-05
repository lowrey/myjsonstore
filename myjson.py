import base64
import requests
from verbose import print_v
from io import BytesIO
import urllib.parse as urlparse
import json
import re
import sys
from os import path

ROOT_URL = "https://api.myjson.com/"
ENCODING = "utf-8"


def file_to_b64(infile):
    f = open(infile, 'rb')
    outfile = BytesIO()
    base64.encode(f, outfile)
    f.close()
    return str(outfile.getvalue(), ENCODING)


def file_from_b64(b64data, outfile):
    f = open(outfile, 'w+b')
    to_decode = BytesIO()
    to_decode.write(bytes(b64data, ENCODING))
    to_decode.seek(0)
    base64.decode(to_decode, f)
    f.close()


class Post:
    POST_URL = "/bins"

    def route(self, opts):
        if opts.file:
            print(self.file(opts.file))
            return
        if not opts.input:
            data = sys.stdin.read()
        else:
            data = opts.input
        print(self.content(data, isStr=True))

    def file(self, infile, fname=None):
        if not fname:
            fname = path.basename(infile)
        fstr = file_to_b64(infile)
        return self.content({"name": fname, "data": fstr})

    def content(self, obj, isStr=False):
        url = urlparse.urljoin(ROOT_URL, self.POST_URL)
        if isStr:
            payload = obj
        else:
            payload = json.dumps(obj)
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, data=payload, headers=headers)
        r.raise_for_status()
        resp = r.json()
        print_v("POST successful: {}".format(resp["uri"]))
        m = re.search("https://api.myjson.com/bins/(.+)", resp["uri"])
        return m.groups()[0]


class Get:
    GET_URL = "/bins/{}"

    def route(self, opts):
        if opts.file:
            self.file(opts.get, opts.file)
        else:
            print(self.content(opts.get))

    def file(self, bin_id, outdir):
        content = self.content(bin_id)
        fpath = path.join(outdir, content["name"])
        b64data = content["data"]
        file_from_b64(b64data, fpath)
        return fpath

    def content(self, bin_id):
        url = urlparse.urljoin(ROOT_URL, self.GET_URL.format(bin_id))
        r = requests.get(url)
        print_v("GET successful: {}".format(url))
        return json.loads(r.text)


class Put:
    PUT_URL = "/bins/{}"

    def route(self, opts):
        if opts.file:
            self.file(opts.update, opts.file)
            return
        if not opts.input:
            data = sys.stdin.read()
        else:
            data = opts.input
        self.content(opts.update, data, isStr=True)

    def file(self, bin_id, infile, fname=None):
        if not fname:
            fname = path.basename(infile)
        fstr = file_to_b64(infile)
        return self.content(bin_id, {"name": fname, "data": fstr})

    def content(self, bin_id, obj, isStr=False):
        url = urlparse.urljoin(ROOT_URL, self.PUT_URL.format(bin_id))
        if isStr:
            payload = obj
        else:
            payload = json.dumps(obj)
        headers = {'Content-Type': 'application/json'}
        r = requests.put(url, data=payload, headers=headers)
        r.raise_for_status()
        print_v("PUT successful: {}".format(url))
