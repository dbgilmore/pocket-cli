import requests
import json
import pocket_constants
import pprint


class PocketAdd:

    def __init__(self):
        pass

    def getUrl(self):
        return raw_input('Please enter the url of the article you would like to add')

    def add(self):
        """
        Adds an article to Pocket
        """

        url = self.getUrl()
        oPayload = {
            'access_token': pocket_constants.strToken,
            'consumer_key': pocket_constants.strConsumerKey,
            'url': url}

        oResponse = requests.post(pocket_constants.strAddURL,
                                  data=json.dumps(oPayload),
                                  headers=pocket_constants.oHeaders)

        return json.loads(oResponse.text)
