import pocket_constants
from pocket_retrieve import PocketRetrieve
from pocket_modify import PocketModify
from pocket_time_tagger import PocketTimeTagger


class Pocket:

    def __init__(self):
        self.pocketRetriever = PocketRetrieve()
        self.pocketModifier = PocketModify()
        self.pocketTimeTagger = PocketTimeTagger()
        self.programRunning = True

    def mapInitialInput(self, x):
        return {
            'R': self.pocketRetriever.preRetrieve,
            'A': self.fakeNews,
            'M': self.pocketModifier.preModify,
            'T': self.pocketTimeTagger.tagUntaggedItems,
            'E': self.terminate
        }.get(x, self.whatDoesTheUserWantToDo)

    def fakeNews(self):
        print 'fake news'

    def terminate(self):
        self.programRunning = False

    def whatDoesTheUserWantToDo(self):
        while self.programRunning:
            print pocket_constants.retrieveText
            print pocket_constants.addText
            print pocket_constants.modifyText
            print pocket_constants.tagUntaggedItemsText
            print pocket_constants.exitText
            selectedOption = raw_input('Please select one of the ''
                                       'above options: ').upper()
            self.mapInitialInput(selectedOption)()


if __name__ == '__main__':
    Pocket().whatDoesTheUserWantToDo()
