import os
import re
import json

def load_directory(path):
    ret = {}

    for f in os.listdir(path):
        m = re.match('^(.*)\.json$', f)
        if m:
            ret[m.group(1)] = json.load(open(path + '/' + f))

    return ret
