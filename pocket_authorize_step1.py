import requests
import json
import webbrowser

def auth():
    url='https://getpocket.com/v3/oauth/request'
    payload = {'consumer_key':'66916-1b15c9e7b794b61fa7840d73', 'redirect_uri':'https://google.com'}
    headers = {'content-type':'application/json', 'charset':'UTF-8', 'X-Accept': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    resp = json.loads(response.text)
    return resp.get('code')

def redirect(request_token):

  url = 'https://getpocket.com/auth/authorize?request_token='+request_token+'&redirect_uri=https://getpocket.com'
  chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

  webbrowser.get(chrome_path).open(url)

def authorize(access_code):
    print access_code
    url = 'https://getpocket.com/v3/oauth/authorize'
    payload = {'code':access_code,'consumer_key':'66916-1b15c9e7b794b61fa7840d73'}
    headers = {'content-type':'application/json', 'charset':'UTF-8', 'X-Accept': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print response.text
    print response
    #return resp.get('code')


access_code = auth()
redirect(access_code)
print access_code
