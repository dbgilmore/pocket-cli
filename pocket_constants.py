import pocket_token
"""
Pocket Constants
"""


stateArchived = {'state':'archive'}
stateUnread = {'state':'unread'}
stateAll = {'state':'all'}

favourited = {'favorite':1}
notFavourited = {'favorite':0}

untagged = {'tag':'_untagged_'}
tag = {'tag':'_to_be_replaced_'}

contentTypeArticle = {'contentType':'article'}
contentTypeVideo = {'contentType':'video'}
contentTypeImage = {'contentType':'image'}

sortNewest = {'sort':'newest'}
sortOldest = {'sort':'oldest'}
sortTitle = {'sort':'title'}
sortSite = {'sort':'nsite'}

detailTypeSimple = {'detailType':'simple'}
detailTypeComplete = {'detailType':'complete'}

search = {'search':'_to_be_replaced_'}
domain = {'domain':'_to_be_replaced_'}
since = {'since':'_to_be_replaced_'}
count = {'count':'_to_be_replaced_'}
offset = {'offset':'_to_be_replaced_'}

strToken = pocket_token.strToken
strConsumerKey = '66916-1b15c9e7b794b61fa7840d73'
iWordsPerMinute = 250
iRoundBase = 5
strUntagged = '_untagged_'
oHeaders = {'content-type':'application/json', 'charset':'UTF-8', 'X-Accept': 'application/json'}
strRetrieveURL = 'https://getpocket.com/v3/get'
strModifyURL = 'https://getpocket.com/v3/send'
strAddURL = 'https://getpocket.com/v3/add'

retrieveText = '(R)etrieve some articles'
modifyText = '(M)odify an existing article in Pocket'
addText = '(A)dd an article to Pocket'
