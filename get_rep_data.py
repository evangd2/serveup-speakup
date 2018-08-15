import urllib
import json

from google.appengine.api import urlfetch
#from collections import OrderedDict

addr_keys = ["line1", "line2", "line3", "city", "state", "zip"]

def get_rep_data(request_params):
    encoded_params = urllib.urlencode(request_params, True)
    rep_data = urlfetch.fetch("https://www.googleapis.com/civicinfo/v2/representatives?{}"
    .format(encoded_params)).content
    rep_data = json.loads(rep_data)
    if "error" not in rep_data:
        for rep in rep_data["officials"]:
            rep["address"] = "; ".join([ format_addr(addr) for addr in rep["address"] ])
            rep["phones"] = ", ".join(rep["phones"])
        return rep_data
    else:
        return {}

def format_addr(addr):
    address = ""
    for key in addr_keys:
        if key in addr:
            field = addr[key]
            if key == "state":
                address += field + " "
            elif key == "zip":
                address += field
            else:
                address += field + ", "
    return address
