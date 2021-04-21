from glob import glob
import json


def remove_options_field_from_json(folder_path):
    for filename in sorted(glob(folder_path + '/*.json')):
        print(filename)
        with open(filename, 'r') as f:
            data = json.load(f)
            if 'options' in data:
                del data['options']

        with open(filename, 'w') as f:
            json.dump(data, f)
