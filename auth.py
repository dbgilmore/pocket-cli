import requests
import os.path
import json
import webbrowser
import time

AUTH_URL = ("https://getpocket.com/auth/authorize?"
            "request_token=%s&redirect_uri=%s")
REQUEST_TOKEN_URL = "https://getpocket.com/v3/oauth/request"
AUTH_TOKEN_URL = "https://getpocket.com/v3/oauth/authorize"
REDIRECT_URL = "http://www.success.com"
CONFIG_FILE = '.creds'
access_token = None
consumer_key = None


def auth():
    if os.path.isfile(CONFIG_FILE) is not True:
        with open(CONFIG_FILE, "w+") as creds_file:
            creds_file.write('{"access_token":"token","consumer_key":"key","since":"since"}')

    with open(CONFIG_FILE, "r+") as creds_file:
        creds = json.loads(creds_file.read())

    access_token = None

    if creds['consumer_key'] == 'key':
        creds['consumer_key'] = raw_input("Please paste your consumer_key "
                                          "and please enter: ")
        consumer_key = creds['consumer_key']
    else:
        consumer_key, access_token = get_creds_from_file(creds)
        print "You are already authorized."

    if not access_token:
        access_token, username = access_token_flow(consumer_key)
        print "SUCCESS."

    config = ('{"consumer_key":"' + consumer_key +
              '","access_token":"' + access_token +
              '","since":0}')

    with open(CONFIG_FILE, 'w') as creds_file:
        creds_file.write(config)

    with open(CONFIG_FILE, 'r') as creds_file:
        creds = json.loads(creds_file.read())
    return creds


def access_token_flow(consumer_key):
    code = get_authentication_code(consumer_key)
    redirect_user(code)
    return get_access_token(consumer_key, code)


def get_authentication_code(consumer_key):
    payload = {'consumer_key': consumer_key, 'redirect_uri': REDIRECT_URL}
    headers = {'content-type': 'application/json',
               'charset': 'UTF-8', 'X-Accept': 'application/json'}

    response = requests.post(REQUEST_TOKEN_URL,
                             data=json.dumps(payload),
                             headers=headers)
    resp = json.loads(response.text)
    return resp.get('code')


def redirect_user(code):
    chrome_path = get_chrome_path()
    print 'Please follow the instructions in the web browser that is about '
    'to open, then return here'
    raw_input("Press enter to proceed.")
    url = AUTH_URL % (code, REDIRECT_URL)
    print url

    webbrowser.get(chrome_path).open(url)
    raw_input('Please press enter once the browser has redirected you '
              'to ' + REDIRECT_URL + ':')


def get_chrome_path():
    while True:
        print 'Which Operating System are you running?'
        print '1: Windows'
        print '2: Mac OS X'
        print '3: Linux'
        input = raw_input()

        if (input == '1'):
            return 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        elif (input == '2'):
            return 'open -a /Applications/Google\ Chrome.app %s'
        elif (input == '3'):
            return 'google-chrome'
        else:
            print 'Incorrect choice. Please try again'


def get_access_token(consumer_key, code):
    payload = {'code': code, 'consumer_key': consumer_key}
    headers = {'content-type': 'application/json',
               'charset': 'UTF-8',
               'X-Accept': 'application/json'}

    response = requests.post(AUTH_TOKEN_URL,
                             data=json.dumps(payload),
                             headers=headers)
    body = response.json()
    return body["access_token"], body["username"]


def get_creds_from_file(config):
    return (config['consumer_key'], config['access_token'])


if __name__ == "__main__":
    auth()
