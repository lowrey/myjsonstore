import base64
import requests
from verbose import print_v  # , write_v
from io import BytesIO
import urllib.parse as urlparse
import json
import re
import sys
from os import path

ROOT_URL = "https://api.myjson.com/"
ENCODING = "utf-8"


class Post:
    POST_URL = "/bins"

    def post(self, opts):
        if opts.file:
            self.file(opts.file)
            return
        data = ""
        if not opts.input:
            data = sys.stdin.read()
        else:
            data = opts.input
        self.content(data)

    @staticmethod
    def file_tob64(infile):
        f = open(infile, 'rb')
        outfile = BytesIO()
        base64.encode(f, outfile)
        f.close()
        return str(outfile.getvalue(), ENCODING)

    def file(self, infile):
        fname = path.basename(infile)
        fstr = self.file_tob64(infile)
        return self.content({"name": fname, "data": fstr})

    def content(self, obj):
        url = urlparse.urljoin(ROOT_URL, self.POST_URL)
        payload = json.dumps(obj)
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, data=payload, headers=headers)
        r.raise_for_status()
        resp = r.json()
        print_v("Request successful: {}".format(resp["uri"]))
        m = re.search("https://api.myjson.com/bins/(.+)", resp["uri"])
        return m.groups()[0]


class Get:
    GET_URL = "/bins/{}"

    # route to appropriate function
    def get(self, dest, opts):
        if opts.file:
            self.file(dest, opts.file)
        else:
            print(self.content(dest))

    # get a file encoded in b64
    def file(self, bin_id, outdir):
        data = self.content(bin_id)
        fpath = path.join(outdir, data["name"])
        f = open(fpath, 'w+b')
        to_decode = BytesIO()
        to_decode.write(bytes(data["data"], ENCODING))
        to_decode.seek(0)
        base64.decode(to_decode, f)
        f.close()
        return fpath

    def content(self, bin_id):
        url = urlparse.urljoin(ROOT_URL, self.GET_URL.format(bin_id))
        r = requests.get(url)
        print_v("Get successful")
        return json.loads(r.text)
