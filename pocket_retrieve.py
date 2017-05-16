import requests
import json
import pocket_constants
import pprint


class PocketRetrieve:

    def __init__(self):
        pass

    def preRetrieve(self):
        optionParams = {}
        print pocket_constants.retrieveOptions
        choices = raw_input('Please input your choices from the above, '
                            'separated by comma: ').lower()
        choiceslist = choices.replace(' ', '').split(',')

        for choice in choiceslist:

            response = self.mapRetrieveInput(choice)
            # Nasty hack - check if the returned thing is a function.
            # If it is, call it
            if callable(response):
                response = response()

            optionParams[choice] = response.get(choice)

            if response.get(choice) == '_to_be_replaced_':
                optionParams[choice] = raw_input('Please enter a '
                                                 'value for ' + choice + ':')

        return self.retrieve(optionParams)

    def retrieve(self, optionalParameters=None):
        """
        Retrieve list of articles from Pocket.
        """

        oPayload = {
            'access_token': pocket_constants.strToken,
            'consumer_key': pocket_constants.strConsumerKey}

        if optionalParameters is not None:
            for param in optionalParameters:
                oPayload[param] = optionalParameters[param]

        oResponse = requests.post(pocket_constants.strRetrieveURL,
                                  data=json.dumps(oPayload),
                                  headers=pocket_constants.oHeaders)
        #  TODO do something more with the response

        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(json.loads(oResponse.text))
        return json.loads(oResponse.text)

    def mapRetrieveInput(self, x):
        matchedInput = {
            'state': self.mapState,
            'favorite': self.mapFavorited,
            'tag': pocket_constants.tag,
            'untagged': pocket_constants.untagged,
            'contenttype': self.mapContentType,
            'sort': self.mapSort,
            'detailtype': self.mapDetailType,
            'search': pocket_constants.search,
            'domain': pocket_constants.domain,
            'since': pocket_constants.since,
            'count': pocket_constants.count,
            'offset': pocket_constants.offset
        }.get(x, "No match")
        if matchedInput == 'No match':
            return self.preRetrieve()
        else:
            return matchedInput

    def mapState(self):
        print '(All, Archived, Unread)'
        state = raw_input('Please enter the state you would like to '
                          'retrieve: ').lower()
        matchedState = {
            'all': pocket_constants.stateAll,
            'archived': pocket_constants.stateArchived,
            'unread': pocket_constants.stateUnread
        }.get(state, "No match")
        if matchedState == 'No match':
            return self.mapState()
        else:
            return matchedState

    def mapFavorited(self):
        print '(Favorited, Not Favorited)'
        favorite = raw_input('Please enter the favorited state you would '
                             'like to retrieve: ').lower()
        matchedFavorite = {
            'favorited': pocket_constants.favorited,
            'not favorited': pocket_constants.notFavorited
        }.get(favorite, "No match")
        if matchedFavorite == 'No match':
            return self.mapFavorited()
        else:
            return matchedFavorite

    def mapContentType(self):
        print '(Article, Image, Video)'
        contentType = raw_input('Please enter the content type you would '
                                'like to retrieve: ').lower()
        matchedContentType = {
            'article': pocket_constants.contentTypeArticle,
            'image': pocket_constants.contentType,
            'video': pocket_constants.contentTypeVideo
        }.get(contentType, "No match")
        if matchedContentType == 'No match':
            return self.mapContentType()
        else:
            return matchedContentType

    def mapSort(self):
        print '(newest, oldest, site, title)'
        sort = raw_input('Please enter the sorting you would '
                         'like to apply: ').lower()
        matchedSort = {
            'newest': pocket_constants.sortNewest,
            'oldest': pocket_constants.sortOldest,
            'site': pocket_constants.sortSite,
            'title': pocket_constants.sortTitle
        }.get(sort, "No match")
        if matchedSort == 'No match':
            return self.mapSort()
        else:
            return matchedSort

    def mapDetailType(self):
        print '(simple, complete)'
        detailType = raw_input('Please enter the detail level you would '
                               'like to retrieve: ').lower()
        matchedDetailType = {
            'simple': pocket_constants.detailTypeSimple,
            'complete': pocket_constants.detailTypeComplete
        }.get(detailType, "No match")
        if matchedDetailType == 'No match':
            return self.mapDetailType()
        else:
            return matchedDetailType

    def postRetrieve():
        pass
