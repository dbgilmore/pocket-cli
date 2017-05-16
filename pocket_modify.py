import requests
import json
import pocket_constants
from pocket_retrieve import PocketRetrieve


class PocketModify:

    def __init__(self):
        self.pocketRetriever = PocketRetrieve()

    def preModify(self, oJSONPayload):
        self.modify(oJSONPayload)

    def modify(self, oActions):
        oPayload = {'access_token': pocket_constants.strToken,
                    'consumer_key': pocket_constants.strConsumerKey,
                    'actions': oActions}

        requests.post(pocket_constants.strModifyURL,
                      data=json.dumps(oPayload),
                      headers=pocket_constants.oHeaders)
        return

    def postModify(self):
        pass
