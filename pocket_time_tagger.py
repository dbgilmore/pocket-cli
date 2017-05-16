from pocket_retrieve import PocketRetrieve
from pocket_modify import PocketModify
import pocket_constants


class PocketTimeTagger:

    def __init__(self):
        self.pocketRetriever = PocketRetrieve()
        self.pocketModifier = PocketModify()

    def generateTag(self, oArticle):
        """
        Generate a tag based on word count of the article, rounded to nearest
        five minutes.
        """
        iWordCount = int(oArticle['word_count'])
        strTag = self.rounder(iWordCount / pocket_constants.iWordsPerMinute)
        if strTag < 15:
            strTag = 'short_reads'
        oJSONTag = {'action': 'tags_add',
                    'item_id': oArticle['item_id'],
                    'tags': strTag}
        return oJSONTag

    def rounder(self, iNumber):
        """
        Round estimated reading time to the nearest five minutes, to avoid too
        many tags.
        """
        return int(pocket_constants.iRoundBase *
                   round(float(iNumber)/pocket_constants.iRoundBase))

    def tagUntaggedItems(self):
        """
        Do the thing.
        """
        oArticles = self.pocketRetriever.retrieve(pocket_constants.untagged)
        oJSONPayload = []
        for oArticle in oArticles.get('list').items():
            if oArticle[1]['is_article'] == '1':
                oJSONPayload.append(self.generateTag(oArticle[1]))
        self.pocketModifier.preModify(oJSONPayload)
