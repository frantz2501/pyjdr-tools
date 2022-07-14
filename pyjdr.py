import os
import json
import random
from conf import *
from secrets import *
import requests

def openFolder(folderPath):
    filesList = os.listdir(folderPath)
    return filesList


def extractData(sfile, myPath):
    with open(os.path.join(myPath, sfile), 'r') as f:
        data = f.readlines()
        return list(data)


def randomize(mylist):
    return random.choice(tuple(mylist))


def kankaExport(line, asset, cid):
    url = BASEURL + cid + "/" + asset + "/"

    data = dict()
    data['name'] = NAME_PREF + line['nom']
    data['type'] = TYPE
    #data['charges'] = line['niveau']
    data['entry'] = line['desc']

    payload = json.dumps({
        "name": data['name'],
        "type": data['type'],
        #"charges": data['charges'],
        "entry": data['entry']
    })
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + ptoken
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

    return response