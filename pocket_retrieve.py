import requests
import json
import pocket_constants
class PocketRetrieve:

    def __init__(self):
        pass

    def retrieve(self,optionalParameters=None):
        """
        Retrieve list of articles from Pocket.
        """

        oPayload = {'access_token':pocket_constants.strToken,'consumer_key':pocket_constants.strConsumerKey}
        if optionalParameters!=None:
            for param in optionalParameters:
                for key in param:
                    oPayload[key] = param[key]

        oResponse = requests.post(pocket_constants.strRetrieveURL, data=json.dumps(oPayload), headers=pocket_constants.oHeaders)
        return json.loads(oResponse.text)

    def generateTag(self,oArticle):
        """
        Generate a tag based on word count of the article, rounded to nearest
        five minutes.
        """
        iWordCount = int(oArticle['word_count'])
        strTag = self.rounder(iWordCount / pocket_constants.iWordsPerMinute)
        if strTag < 15:
            strTag = 'short_reads'
        oJSONTag = {'action':'tags_add','item_id': oArticle['item_id'],'tags':strTag}
        return oJSONTag

    def sendRequest(self,oActions):
        """
        Send request to Pocket with tags to add to articles.  Send as batch to
        avoid hitting rate limiter.
        """
        oPayload = {'access_token':pocket_constants.strToken,'consumer_key':pocket_constants.strConsumerKey,'actions':oActions}

        requests.post(pocket_constants.strModifyURL, data=json.dumps(oPayload), headers=pocket_constants.oHeaders)
        return

    def rounder(self,iNumber):
        """
        Round estimated reading time to the nearest five minutes, to avoid too
        many tags.
        """
        return int(pocket_constants.iRoundBase * round(float(iNumber)/pocket_constants.iRoundBase))

    def tagUntaggedItems(self):
        """
        Do the thing.
        """
        oArticles = self.retrieve([pocket_constants.untagged])
        oJSONPayload = []
        for oArticle in oArticles.get('list').items():
            if oArticle[1]['is_article'] == '1':
                oJSONPayload.append(self.generateTag(oArticle[1]))
        self.sendRequest(oJSONPayload)

    def writeArticlesToFile(tag=None):
        if tag:
            strFilename = tag+"Articles.txt"
        else:
            strFilename = "Articles.json"
        file_object = open(strFilename, "a")
        file_object.write(json.dumps(retrieve(tag)))

    def writeArchiveToFile():
        strFilename = "Archive.json"
        file_object = open(strFilename, "a")
        file_object.write(json.dumps(retrieve()))
