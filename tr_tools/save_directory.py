import json

def save_directory(path, data):
    for lang, trans in data.items():
        json.dump(
            trans,
            open(path + '/' + lang + '.json', 'w'),
            indent=2,
            sort_keys=True
        )
