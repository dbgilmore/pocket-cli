import json
"""
Pocket Constants
"""
creds_file = file(".creds", 'r')
creds = json.loads(creds_file.read())
creds_file.close()
strToken = creds['access_token']
strConsumerKey = creds['consumer_key']

stateArchived = {'state': 'archive'}
stateUnread = {'state': 'unread'}
stateAll = {'state': 'all'}

favorited = {'favorite': 1}
notFavorited = {'favorite': 0}

untagged = {'tag': '_untagged_'}
tag = {'tag': '_to_be_replaced_'}

contentTypeArticle = {'contentType': 'article'}
contentTypeVideo = {'contentType': 'video'}
contentTypeImage = {'contentType': 'image'}

sortNewest = {'sort': 'newest'}
sortOldest = {'sort': 'oldest'}
sortTitle = {'sort': 'title'}
sortSite = {'sort': 'site'}

detailTypeSimple = {'detailType': 'simple'}
detailTypeComplete = {'detailType': 'complete'}

search = {'search': '_to_be_replaced_'}
domain = {'domain': '_to_be_replaced_'}
since = {'since': '_to_be_replaced_'}
count = {'count': '_to_be_replaced_'}
offset = {'offset': '_to_be_replaced_'}

iWordsPerMinute = 250
iRoundBase = 5
strUntagged = '_untagged_'
oHeaders = {'content-type': 'application/json',
            'charset': 'UTF-8', 'X-Accept': 'application/json'}
strRetrieveURL = 'https://getpocket.com/v3/get'
strModifyURL = 'https://getpocket.com/v3/send'
strAddURL = 'https://getpocket.com/v3/add'

retrieveText = '(R)etrieve some articles'
modifyText = '(M)odify an existing article in Pocket'
addText = '(A)dd an article to Pocket'
tagUntaggedItemsText = '(T)ag untagged items based on estimated time to read'
graphifyText = '(G)raphify'
exitText = '(E)xit'

# TODO give more detail
retrieveOptions = """
state - unread, archived, all
favorite - favorited, not favorited
tag - any tag
untagged - untagged items
contentType - articles, images, videos
sort - newest, oldest, site, title
detailType - simple, complete
search - search based on title and url
domain - search on article domain
since - lol timestamp stuff
count - only return X number of items
offset - use with count
"""
