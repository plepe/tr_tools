import json
import sys

def save_directory(path, data):
    for lang, trans in data.items():
        result = json.dumps(
                trans,
                indent=4,
                ensure_ascii=False,
                sort_keys=True
            )

        # compatibility Python2
        if sys.version_info < (3, 0):
            result = result.encode('UTF-8')

        open(path + '/' + lang + '.json', 'w').write(result)
