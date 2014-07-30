from base64 import decode
import requests, StringIO
from verbose import print_v

#get a file encoded in b64
def get_file(pad_name, outfile):
    f = open(outfile, 'w+b')
    to_decode = StringIO.StringIO()
    to_decode.write(get_content(pad_name))
    to_decode.seek(0)
    decode(to_decode, f)
    f.close()

def get_content(bin_id):
    # url =  + pad_name
    r = requests.get(url)
    print_v("Get successful")
    return contents.text(r.text)

#route to appropriate function
def get(dest, opts):
    if opts.file:
        get_file(dest, opts.file)
    else:
        print(get_content(dest))
