import json

def save_json(data, filename='data.json'):
    with open(filename, "w") as outfile:
        json.dump(data, outfile, indent=4)