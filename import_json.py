import json

with open('example.json') as json_file:
    data = json.load(json_file)
    for email in data['thirdparty_recipients']:
        print email
