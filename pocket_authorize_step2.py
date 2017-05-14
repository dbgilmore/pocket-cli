import requests
import json

def authorize():
    access_code = '4f060fab-0384-c17b-eb7f-eba859'
    print access_code
    url = 'https://getpocket.com/v3/oauth/authorize'
    payload = {'code':access_code,'consumer_key':'66916-1b15c9e7b794b61fa7840d73'}
    headers = {'content-type':'application/json', 'charset':'UTF-8', 'X-Accept': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print response.text
    print response

authorize()
