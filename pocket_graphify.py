import pocket_constants
from pocket_retrieve import PocketRetrieve
import json
import plotly
import datetime
from collections import OrderedDict
from plotly.graph_objs import Scatter, Layout, Bar

class PocketGraphify:
    def __init__(self):
        self.pocketRetriever = PocketRetrieve()

    def graphify(self):
        allTheArticles = self.pocketRetriever.retrieve({'state': 'all', 'detailType': 'complete'});

        with open('.pocket_json', "w+") as output:
            output.write(json.dumps(allTheArticles))

        self.graphifyByTag()
        self.graphifyByYearMonth()

    def graphifyByTag(self):

        with open('pocket_json', "r+") as json_file:
          output = json.loads(json_file.read())

        dataRead = {'untagged': 0}
        dataUnread = {'untagged': 0}
        for article in output:
            if output[article].get('time_read') != '0':
                if output[article].get('tags'):
                    tags = output[article].get('tags')
                    for tag in tags:
                        if str(tags[tag]['tag']) in dataRead:
                            dataRead[str(tags[tag]['tag'])] += 1
                        else:
                            dataRead[str(tags[tag]['tag'])] = 1
                else:
                    dataRead['untagged'] += 1
            else:
                if output[article].get('tags'):
                    tags = output[article].get('tags')
                    for tag in tags:
                        if str(tags[tag]['tag']) in dataUnread:
                            dataUnread[str(tags[tag]['tag'])] += 1
                        else:
                            dataUnread[str(tags[tag]['tag'])] = 1
                else:
                    dataUnread['untagged'] += 1

        # This might be doing a weird thing
        dataRead = OrderedDict(sorted(dataRead.items(), key=lambda t: t[0]))
        dataUnread = OrderedDict(sorted(dataUnread.items(), key=lambda t: t[0]))

        xaxisRead = dataRead.keys()
        yaxisRead = dataRead.values()

        xaxisUnread = dataUnread.keys()
        yaxisUnread = dataUnread.values()

        trace1 = Bar(
            x=xaxisRead,
            y=yaxisRead,
            name='Read'
        )
        trace2 = Bar(
            x=xaxisUnread,
            y=yaxisUnread,
            name='Unread'
        )

        plotly.offline.plot({
            "data": [trace1, trace2],
            "layout": Layout(barmode='stack', title="Bar chart showing the number of articles in Pocket per tag", xaxis = {'type': 'category', 'title': 'Tag name'}, yaxis = {'title': 'Number of articles tagged'})
        })

    def graphifyByYearMonth(self):
        with open('pocket_json', "r+") as json_file:
          output = json.loads(json_file.read())

        dataRead = {}
        dataUnread = {}
        for article in output:
            yearMonth = datetime.datetime.fromtimestamp(
                int(output[article].get('time_added'))
            ).strftime('%Y-%m')

            if output[article].get('time_read') != '0':

                if yearMonth in dataRead:
                    dataRead[yearMonth] += 1
                else:
                    dataRead[yearMonth] = 1
            else:
                if yearMonth in dataUnread:
                    dataUnread[yearMonth] += 1
                else:
                    dataUnread[yearMonth] = 1

        dataRead = OrderedDict(sorted(dataRead.items(), key=lambda t: t[0]))
        dataUnreadFull = dict.fromkeys(dataRead.keys(),0)
        for x in dataUnread:
            dataUnreadFull[x] = dataUnread[x]

        xaxisRead = dataRead.keys()
        yaxisRead = dataRead.values()

        xaxisUnread = dataUnreadFull.keys()
        yaxisUnread = dataUnreadFull.values()

        trace1 = Bar(
            x=xaxisRead,
            y=yaxisRead,
            name='Read'
        )
        trace2 = Bar(
            x=xaxisUnread,
            y=yaxisUnread,
            name='Unread'
        )

        plotly.offline.plot({
            "data": [trace1, trace2],
            "layout": Layout(barmode='stack', title="Bar chart showing the number of articles added to Pocket per month", xaxis = {'type': 'category', 'title': 'Month'}, yaxis = {'title': 'Number of articles added'})
        })
