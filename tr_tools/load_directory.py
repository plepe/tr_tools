import os
import re
import json

def load_directory(path):
    ret = {}

    for f in os.listdir(path):
        m = re.match('^(.*)\.json$', f)
        if m:
            lang = m.group(1)
            try:
                ret[lang] = json.load(open(path + '/' + f))
            except ValueError as e:
                print('Warning: Can\'t load translation {}: {}'.format(lang, e))

    return ret
